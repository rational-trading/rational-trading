import { post } from "../request";

interface LoginRequest {
    username: string;
    password: string;
}

class LoginEndpoint {
    async post(username: string, password: string): Promise<string> {
        return post<LoginRequest, string>({ endpoint: "/login", data: { username, password } });
    }
}

export { LoginEndpoint };
