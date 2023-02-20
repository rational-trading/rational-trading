import { HelloEndpoint } from "./hello";
import { MathsEndpoint } from "./maths";
import { PriceRoute } from "./price";

class Api {
    hello(): HelloEndpoint {
        return new HelloEndpoint();
    }

    maths(token: string): MathsEndpoint {
        return new MathsEndpoint(token);
    }

    price(ticker: string): PriceRoute {
        return new PriceRoute(ticker);
    }
}

const api = new Api();

export default api;
