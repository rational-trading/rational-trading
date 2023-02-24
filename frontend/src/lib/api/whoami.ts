import { get } from "../request";

interface WhoamiResponse {
    username: string;
}

class WhoamiEndpoint {
    async get(): Promise<string> {
        return (await get<WhoamiResponse>({ endpoint: "/user/whoami", authenticated: true })).username;
    }
}

export { WhoamiEndpoint };
