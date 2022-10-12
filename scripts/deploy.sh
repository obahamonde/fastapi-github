cd function
serverless plugin install -n serverless-python-requirements
serverless deploy > ../deploy.yml
cd ..
python scripts/redirect.py
yarn build
netlify deploy --prod --dir=dist --message="Deployed from $CIRCLE_BRANCH"
echo "Deployed to Netlify"
