import { get } from "../request";

interface MathsResponse {
    add: number,
    multiply: number,
    authenticated_user: string,
}

class MathsEndpoint {
    token: string;

    constructor(token: string) {
        this.token = token;
    }

    get(a: number, b: number): Promise<MathsResponse> {
        return get<MathsResponse>({ endpoint: `/maths/${a}and${b}`, bearer: this.token });
    }
}

export { MathsEndpoint, type MathsResponse };
