import { HelloEndpoint } from "./hello";
import { MathsEndpoint } from "./maths";
import { PriceRoute } from "./price";
import { LoginEndpoint } from "./login";
import { SignupEndpoint } from "./signup";
import { WhoamiEndpoint } from "./whoami";

class Api {
    login(): LoginEndpoint {
        return new LoginEndpoint();
    }

    signup(): SignupEndpoint {
        return new SignupEndpoint();
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

    whoami(): WhoamiEndpoint {
        return new WhoamiEndpoint();
    }

    pendingRequest<T>() {
        // eslint-disable-next-line @typescript-eslint/no-empty-function
        return new Promise<T>(() => { });
    }
}

const api = new Api();

export default api;
