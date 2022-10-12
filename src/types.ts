export type User = {
    sub: string;
    email?: string;
    username: string;
    picture: string;
    token?: string;
};

export type IRequest = {
    method: 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH' | 'HEAD' | 'OPTIONS';
    url: string;
    headers?: Record<string, string>;
    body?: any;
}

export type IResponse = {
    status: number;
    data: any;
    headers: Record<string, string>;
}
