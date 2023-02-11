import { get, post } from "../request";

interface HelloRequest {
    name: string;
}

class HelloEndpoint {
    async get(name?: string): Promise<string> {
        return get<string>({ endpoint: "/hello/", queryString: name ? `name=${name}` : undefined });
    }

    async post(name: string): Promise<string> {
        return post<HelloRequest, string>({ endpoint: "/hello/", data: { name } });
    }
}

export { HelloEndpoint };
