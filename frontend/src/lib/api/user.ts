import { get } from "../request";

interface User {
    username: string;
}

class UserEndpoint {
    whoami(): Promise<User> {
        return get<User>({ endpoint: "/user/whoami", authenticated: true });
    }
}

export { UserEndpoint };
