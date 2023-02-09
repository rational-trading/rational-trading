import { HelloEndpoint } from "./hello";
import { MathsEndpoint } from "./maths";

class Api {
    hello(): HelloEndpoint {
        return new HelloEndpoint();
    }

    maths(token: string): MathsEndpoint {
        return new MathsEndpoint(token);
    }
}

const api = new Api();

export default api;
