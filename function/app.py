"""Lambda Handler."""
import asyncio
from fastapi import *
from fastapi.responses import *
from fastapi.templating import *
from fastapi.staticfiles import *
from bs4 import BeautifulSoup
from typing import *
from pydantic import *
from datetime import *
from aiohttp import *
from enum import Enum
from os import environ, getenv
from decimal import *
from dotenv import load_dotenv
from aioboto3 import Session
from boto3 import Session as Boto3Session
from boto3.dynamodb.types import Binary
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError, ParamValidationError, BotoCoreError
from json import dumps, loads
from uuid import uuid4
from zipfile import ZipFile


load_dotenv()

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
AUTH0_DOMAIN = getenv("AUTH0_DOMAIN")
AWS_ACCESS_KEY_ID = getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = getenv("AWS_DEFAULT_REGION")
AWS_S3_BUCKET = getenv("AWS_S3_BUCKET")
AWS_SES_EMAIL = getenv("AWS_SES_EMAIL")
FAUNA_SECRET = getenv("FAUNA_SECRET")
GOOGLE_URL = "https://www.google.com/search?q="        
PYPI_URL = "https://pypi.org/search/?q="

entity_types = ["PERSON", "LOCATION", "ORGANIZATION", "COMMERCIAL_ITEM", "EVENT", "DATE", "QUANTITY", "TITLE", "OTHER"]

class WebSite(BaseModel):
    """FOO BAR"""
    html:str

class HTTPClient:   
    """Aiohttp client session"""
    async def html(self,url: str)->str:
        """Fetch HTML from URL."""
        async with ClientSession() as session:
            async with session.get(url=url, headers=HEADERS) as response:
                return await response.text(encoding="utf-8")
            
    async def json(self,url: Union[str,HttpUrl],headers:Dict[str,Any])->Dict[str,Any]:
        """Fetch JSON from URL."""
        async with ClientSession() as session:
            async with session.get(url=url, headers=headers) as response:
                return await response.json()
            
    async def blob(self,url: str)->bytes:
        """Fetch BLOB from URL."""
        async with ClientSession() as session:
            async with session.get(url) as response:
                return await response.read()

    async def soup(self,url:str)->BeautifulSoup:
        """Parse HTML from URL."""
        async with ClientSession() as session:
            async with session.get(url=url, headers=HEADERS) as response:
                html = await response.text(encoding="utf-8")
                return BeautifulSoup(html,"html.parser")

    async def auth(self, req:Request)->Dict[str,Any]:
        """Lambda Authorizer."""
        token = req.headers.get("Authorization").split(" ")[1]
        return await self.json(f"https://{AUTH0_DOMAIN}/userinfo", {"Authorization": f"Bearer {token}"})
    
    
    async def text(self,url: str)->str:
        """Fetch text from URL."""
        async with ClientSession() as session:
            async with session.get(url=url, headers=HEADERS) as response:
                return await response.text(encoding="utf-8")

class DynaModel(BaseModel):
    """Wrapper for DynamoDB"""
    def __init__(self,**data: Any) -> None:
        try:
            super().__init__(**data)  
            boto3_session=Boto3Session(
                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                    region_name=AWS_DEFAULT_REGION)            
            sts = boto3_session.client("sts")
            credentials = sts.get_session_token()["Credentials"]
            self.session = Session(
                aws_access_key_id=credentials["AccessKeyId"],
                aws_secret_access_key=credentials["SecretAccessKey"],
                aws_session_token=credentials["SessionToken"],
                region_name=AWS_DEFAULT_REGION)
        except (ClientError, ParamValidationError, BotoCoreError):
            pass
       
    class Config(BaseConfig):
        """Base Configuration settings for Pydantic models."""
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        extra = Extra.allow
        json_encoders = {
            datetime: str,
            Decimal: float,
            Binary: bytes,
            HttpUrl: str,
            EmailStr: str,
            IPvAnyAddress: str,
            IPvAnyInterface: str,
            IPvAnyNetwork: str
        }

    @property
    def table(self):
        """DynamoDB table name."""
        return self.__class__.__name__.lower()+"s"

    @property
    def pk(self):
        """Primary key."""
        for field in self.__fields__:
            if self.__fields__[field].field_info.extra.get("pk"):
                return self.dict()[field]

    @property
    def sk(self):
        """Sort key."""
        for field in self.__fields__:
            if self.__fields__[field].field_info.extra.get("sk"):
                return self.dict()[field]
    
    @property
    def _pk(self):
        """Partition key field name"""
        for field in self.__fields__:
            if self.__fields__[field].field_info.extra.get("pk"):
                return field
    
    @property
    def _sk(self):
        """Sort key field name"""
        for field in self.__fields__:
            if self.__fields__[field].field_info.extra.get("sk"):
                return field        

    @property
    def gsi(self):
        """Global secondary indexes."""
        gsis: List[str] = []
        for field in self.__fields__:
            if self.__fields__[field].field_info.extra.get("gsi"):
                gsis.append(field)
        return [self.dict()[gsi] for gsi in gsis]   
    
    @property
    def _gsi(self):
        """Global secondary index field name."""
        gsis: List[str] = []
        for field in self.__fields__:
            if self.__fields__[field].field_info.extra.get("gsi"):
                gsis.append(field) 
        return gsis

    async def create_table(self):
        """Create table."""
        async with self.session.client("dynamodb") as client:
            try:
                await client.create_table(
                    TableName=self.table,
                    AttributeDefinitions=[
                        {"AttributeName": self._pk, "AttributeType": "S"},
                        {"AttributeName": self._sk, "AttributeType": "S"},
                    ],
                    KeySchema=[
                        {"AttributeName": self._pk, "KeyType": "HASH"},
                        {"AttributeName": self._sk, "KeyType": "RANGE"},
                    ],
                    BillingMode="PAY_PER_REQUEST",
                )
                await client.get_waiter("table_exists").wait(TableName=self.table)
            except (ClientError, ParamValidationError, BotoCoreError):
                pass

    async def get(self)->Dict[str,Any]:
        """Find unique item by primary key."""
        async with self.session.resource("dynamodb") as dynamodb:
            table = await dynamodb.Table(self.table)
            response = await table.get_item(
                Key={
                    self._pk: self.pk,
                    self._sk: self.sk
                }
            )
            return response.pop("Item")
            
    async def post(self)->Dict[str,Any]:
        """Create new item."""
        async with self.session.resource("dynamodb") as dynamodb:
            table = await dynamodb.Table(self.table)
            await table.put_item(
                Item=self.dict()
            )
            return await self.get()
    
    async def update(self)->Dict[str,Any]:
        """Update item."""
        async with self.session.resource("dynamodb") as dynamodb:
            table = await dynamodb.Table(self.table)
            await table.update_item(
                Key={
                    self._pk: self.pk,
                    self._sk: self.sk
                },
                UpdateExpression="set #n=:v",
                ExpressionAttributeNames={"#n": "name"},
                ExpressionAttributeValues={":v": "new name"}
            )
            return await self.get()
        
    async def delete(self)->Dict[str,Any]:
        """Delete item."""
        async with self.session.resource("dynamodb") as dynamodb:
            table = await dynamodb.Table(self.table)
            await table.delete_item(
                Key={
                    self._pk: self.pk,
                    self._sk: self.sk
                }
            )
            return await self.get()
        
    async def query(self)->Dict[str,Any]:
        """Query items."""
        async with self.session.resource("dynamodb") as dynamodb:
            table = await dynamodb.Table(self.table)
            response = await table.query(
                KeyConditionExpression=Key(self._pk).eq(self.pk)
            )
            return response.pop("Items")
        
    async def scan(self)->List[Dict[str,Any]]:
        """Scan items."""
        async with self.session.resource("dynamodb") as dynamodb:
            table = await dynamodb.Table(self.table)
            response = await table.scan()
            return response.pop("Items")

class APIClient:
    """API Client"""
    base_url:Union[str, AnyHttpUrl] = "https://api.github.com/"
    headers:Dict[str,str] = {"Authorization": f"token {environ.get('API_TOKEN')}"}

    async def get(self, endpoint:str) -> Dict[str,Any]:
        """Get Method override"""
        async with ClientSession() as session:
            async with session.get(self.base_url+endpoint, headers=self.headers) as response:
                return await response.json()
            
    async def post(self, endpoint:str, data:Dict[str,Any]) -> Dict[str,Any]:
        """Post Method override"""
        async with ClientSession() as session:
            async with session.post(self.base_url+endpoint, headers=self.headers, json=data) as response:
                return await response.json()
            
    async def patch(self, endpoint:str, data:Dict[str,Any]) -> Dict[str,Any]:
        """Patch Method override"""
        async with ClientSession() as session:
            async with session.patch(self.base_url+endpoint, headers=self.headers, json=data) as response:
                return await response.json()
            
    async def delete(self, endpoint:str) -> Dict[str,Any]:
        """Delete Method override"""
        async with ClientSession() as session:
            async with session.delete(self.base_url+endpoint, headers=self.headers) as response:
                return await response.json()
            
    async def text(self, endpoint:str) -> str:
        """Get text"""
        async with ClientSession() as session:
            async with session.get(self.base_url+endpoint, headers=self.headers) as response:
                return await response.text(encoding="utf-8")

class App(FastAPI):
    """Main App"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = "Serverless FastAPI"
        self.description = "A serverless implementation of FastAPI framework on top of AWS Lambda"
        self.version = "0.1.0"
        self.fetch = HTTPClient()
        self.templates = Jinja2Templates(directory="templates")
        self.session = Session(
            aws_access_key_id=environ.get("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=environ.get("AWS_SECRET_ACCESS_KEY"),
            region_name=environ.get("AWS_DEFAULT_REGION"))
        
        @self.get("/api/search/pip/{pkg}/{page}")
        async def pip_search(pkg:str, page:int=1):
            """Search for a package on PyPI"""
            try:    
                url = PYPI_URL + pkg + "&page=" + str(page)
                response = await self.fetch.soup(url)
                packages = [package.text for package in response.find_all("span", class_ = "package-snippet__name")]
                versions = [version.text for version in response.find_all("span", class_ = "package-snippet__version")]
                descriptions = [description.text for description in response.find_all("p", class_ = "package-snippet__description")]
                data= [{"name":p, "version":v, "description":d} for  p,v,d in zip(packages,versions,descriptions)]
                print(data)
                return data
            except Exception as e:
                print(e)
                return {"error":str(e)}
            
        @self.get("/api/search/{lang}/{query}/{page}")
        async def google_search(lang:str, query:str, page:int)->List[Dict[str,Any]]:
                """Search for a query on Google"""
                try:
                    response = await self.fetch.html(url=f"https://www.google.com/search?q={query}&lr=lang_{lang}&start={str(page*10)}")
                    urls = [link.find("a")["href"] for link in BeautifulSoup(response, "html.parser").find_all("div", class_="yuRUbf")]
                    summaries = [link.find("h3").text for link in BeautifulSoup(response, "html.parser").find_all("div", class_="yuRUbf")]   
                    response = [{"url":i, "summary":j} for i,j in zip(urls, summaries)]
                    print(response)
                    return response
                except Exception as exception:
                    print(exception)
                    raise HTTPException(status_code=500, detail=str(exception))

        @self.get("/api/search/scrap/{domain}")        
        async def scrap_content(domain: str)->Dict[str,Any]:
            """Scraping results."""
            url = f"http://{domain}"
            _soup = await self.fetch.soup(url)
            scripts = [script.src or script.text for script in _soup.find_all("script")] + [script.attrs["src"] for script in _soup.find_all("script") if script.attrs.get("src")]
            styles = [style.text for style in _soup.find_all("style")] + [style.attrs["href"] for style in _soup.find_all("link") if style.attrs.get("href")]
            links = [link.attrs["href"] for link in _soup.find_all("a") if link.attrs.get("href")]
            for link in links:
                if link.startswith("/"):
                    links[links.index(link)] = url + link
                elif link.startswith("http"):
                    pass
                else:
                    links.remove(link)
            images = [image.attrs["src"] for image in _soup.find_all("img") if image.attrs.get("src")]
            for image in images:
                if image.startswith("/"):
                    images[images.index(image)] = url + image
                elif image.startswith("http"):
                    pass
                else:
                    images.remove(image)
            return  loads(dumps({"url": url, "scripts": scripts, "styles": styles, "links": links, "images": images}))

        @self.get("/")
        async def root(request: Request):
            return RedirectResponse(url="http://localhost:3000/")

        @self.get("/api")
        async def api():
            return {"message": "Hello from FastAPI"}

        @self.get("/api/auth")
        async def auth_endpoint(user=Depends(self.fetch.auth))->Dict[str,Any]:
            return user

        @self.get("/api/html")
        async def html():
            return self.templates.TemplateResponse("index.html", {"request": {}})

        @self.get("/api/python")
        async def python():
            return self.templates.TemplateResponse("app.py", {"request": {}})

        @self.get("/api/lib")
        async def html_lib():
            return self.templates.TemplateResponse("lib.html", {"request": {}})

        @self.post("/api/function")
        async def lambda_endpoint(user=Depends(self.fetch.auth), file:UploadFile=File(...))->Union[HttpUrl,str]:
            zip_file = await file.read()
            async with self.session.client("lambda") as lambda_:
                response = await lambda_.create_function(
                    FunctionName=user.sub,
                    Runtime="python3.8",
                    Role="arn:aws:iam::992472819525:role/service-role/search-role-x0hu2si7",
                    Handler="app.handler",
                    Code={
                        "ZipFile": zip_file,
                        },
                    Timeout=3,
                    MemorySize=128,
                    Publish=True  
                )
                url = await lambda_.create_function_url_config(
                    FunctionName= response["FunctionName"],
                    AuthType="NONE",
                    Cors={
                        "AllowOrigins": ["*"],
                        "AllowMethods": ["*"],
                        "AllowHeaders": ["*"],
                        "AllowCredentials": True,
                        "ExposeHeaders": ["*"],
                        "MaxAge": 86400
                    }
                )
                await lambda_.add_permission(
                    FunctionName=response["FunctionName"],
                    StatementId=response["FunctionName"],
                    Action="lambda:InvokeFunctionUrl",
                    Principal="*",
                    FunctionUrlAuthType="NONE"
                )
                return url["FunctionUrl"]

        @self.post("/api/website")
        async def website_endpoint(website:WebSite, user=Depends(self.fetch.auth))->Union[HttpUrl,str]:
            async with self.session.client("s3") as s3:
                sub = user['sub']
                response = await s3.put_object(
                    Bucket=AWS_S3_BUCKET,
                    Key=f"{sub}/index.html",
                    Body=website.html.encode("utf-8"),
                    ACL="public-read",
                    ContentType="text/html"
                )
                print(response)
                return f"https://s3.amazonaws.com/{AWS_S3_BUCKET}/{sub}/index.html"

        @self.post("/api/upload/{key}")
        async def upload(key:str,file:UploadFile = File(...))->None:
            async with self.session.client("s3") as client:
                await client.put_object(Body=file.file.read(), Bucket=AWS_S3_BUCKET, Key=f"{key}/{file.filename}", ACL="public-read", ContentType=file.content_type)

        @self.get("/api/upload")
        async def list_uploads(user=Depends(self.fetch.auth)):
            async with self.session.client("s3") as client:
                response = await client.list_objects_v2(Bucket=AWS_S3_BUCKET, Prefix=user["sub"])
                response.pop("ResponseMetadata")
                data = [f"https://{AWS_S3_BUCKET}.s3.amazonaws.com/{item['Key']}" for item in response["Contents"] if len(response["Contents"]) > 0] if response.get("Contents") else []
                return data
                
        @self.delete("/api/upload")
        async def delete_upload(url:str, user=Depends(self.fetch.auth)):
            async with self.session.client("s3") as client:
                try:
                    await client.delete_object(Bucket=AWS_S3_BUCKET, Key=url.split(f"https://{AWS_S3_BUCKET}.s3.amazonaws.com/")[1])
                except Exception as exception:
                    raise HTTPException(status_code=500, detail=str(exception))

        @self.get("/api/email")
        async def send_email_endpoint(email:EmailStr, subject:str, message:str)->bool:
            async with self.session.client("ses") as client:
                try:
                    await client.send_email(
                        Source=AWS_SES_EMAIL,
                        Destination={
                            "ToAddresses": ["oscar.bahamonde@hatarini.com"]
                        },
                        Message={
                            "Subject": {
                                "Data":email + " - " + subject
                            },
                            "Body": {
                                "Text": {
                                    "Data": message
                                }
                            }
                        }
                    )
                    return True
                except Exception as exception:
                    raise HTTPException(status_code=500, detail=str(exception))
    
        @self.get("/api/chat")
        async def chatbot(message:str)->str:
            async with self.session.client("comprehend") as client:
                entities = await client.detect_entities(Text=message, LanguageCode="en")
                entities.pop("ResponseMetadata")
                sentiments = await client.detect_sentiment(Text=message, LanguageCode="en")
                sentiments.pop("ResponseMetadata")
                for sentetiment in sentiments["SentimentScore"]:
                    sentiments["SentimentScore"][sentetiment] = round(sentiments["SentimentScore"][sentetiment], 2)
                sentiment_score = str(float(sentiments["SentimentScore"][sentiments["Sentiment"].lower().capitalize()])*100)+"%"
                sentiment_type = sentiments["Sentiment"]
                entities = [entity for entity in entities["Entities"] if entity["Type"] in entity_types]
                if len(entities) > 0:
                    text = f"Your message is {sentiment_score} {sentiment_type} and you are talking about {', '.join([entity['Text'] for entity in entities])}."
                else:
                    text = f"Your message is {sentiment_score} {sentiment_type}."
                return text
            
        @self.get("/api/translate/{source}/{target}/{text}")
        async def translate_endpoint(source:str, target:str, text:str)->str:
            async with self.session.client("translate") as client:
                try:
                    response = await client.translate_text(Text=text, SourceLanguageCode=source, TargetLanguageCode=target)
                    return response["TranslatedText"]
                except Exception as exception:
                    raise HTTPException(status_code=500, detail=str(exception))

app = App()
