import { PriceRoute } from "./price";
import { AuthEndpoint } from "./auth";
import { UserEndpoint } from "./user";
import { PortfolioRoute } from "./portfolio";

class Api {
    auth(): AuthEndpoint {
        return new AuthEndpoint();
    }

    user(): UserEndpoint {
        return new UserEndpoint();
    }

    price(ticker: string): PriceRoute {
        return new PriceRoute(ticker);
    }

    portfolio(): PortfolioRoute {
        return new PortfolioRoute();
    }

    pendingRequest<T>() {
        // eslint-disable-next-line @typescript-eslint/no-empty-function
        return new Promise<T>(() => { });
    }
}

const api = new Api();

export default api;
