import { post } from "../request";
import type { TokenSchema } from "../types";

interface LoginRequest {
    username: string;
    password: string;
}

class LoginEndpoint {
    async post(username: string, password: string): Promise<string> {
        return (await post<LoginRequest, TokenSchema>({ endpoint: "/login", data: { username, password } })).access_token;
    }
}

export { LoginEndpoint };
