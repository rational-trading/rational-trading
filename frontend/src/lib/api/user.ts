import { get } from "../request";

interface WhoamiResponse {
    username: string;
}

class UserEndpoint {
    async whoami(): Promise<string> {
        return (await get<WhoamiResponse>({ endpoint: "/user/whoami", authenticated: true })).username;
    }
}

export { UserEndpoint };
