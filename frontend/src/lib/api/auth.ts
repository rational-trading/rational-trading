import { post } from "../request";
import type { TokenSchema } from "../types";

interface LoginSignupRequest {
    username: string;
    password: string;
}

class AuthEndpoint {
    async login(username: string, password: string): Promise<string> {
        return (await post<LoginSignupRequest, TokenSchema>({ endpoint: "/login", data: { username, password } })).access_token;
    }

    async signup(username: string, password: string): Promise<string> {
        return (await post<LoginSignupRequest, TokenSchema>({ endpoint: "/signup", data: { username, password } })).access_token;
    }
}

export { AuthEndpoint };
