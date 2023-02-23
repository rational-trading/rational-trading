import { post } from "../request";
import type { TokenSchema } from "../types";

interface SignupRequest {
    username: string;
    password: string;
}

class SignupEndpoint {
    async post(username: string, password: string): Promise<string> {
        return (await post<SignupRequest, TokenSchema>({ endpoint: "/signup", data: { username, password } })).access_token;
    }
}

export { SignupEndpoint };
