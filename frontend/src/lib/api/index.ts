import { HelloEndpoint } from "./hello";
import { MathsEndpoint } from "./maths";
import { PriceRoute } from "./price";
import { AuthEndpoint } from "./auth";
import { UserEndpoint } from "./user";

class Api {
    auth(): AuthEndpoint {
        return new AuthEndpoint();
    }

    user(): UserEndpoint {
        return new UserEndpoint();
    }

    hello(): HelloEndpoint {
        return new HelloEndpoint();
    }

    maths(token: string): MathsEndpoint {
        return new MathsEndpoint(token);
    }

    price(ticker: string): PriceRoute {
        return new PriceRoute(ticker);
    }

    pendingRequest<T>() {
        // eslint-disable-next-line @typescript-eslint/no-empty-function
        return new Promise<T>(() => { });
    }
}

const api = new Api();

export default api;
