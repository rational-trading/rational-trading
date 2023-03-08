import { PriceRoute } from "./price";
import { AuthEndpoint } from "./auth";
import { UserEndpoint } from "./user";
import { PortfolioRoute } from "./portfolio";
import { TradesRoute } from "./trades";
import { NewsRoute } from "./news";
import { StocksRoute } from "./stocks";
import { FinancialsRoute } from "./financials";

class Api {
    auth(): AuthEndpoint {
        return new AuthEndpoint();
    }

    financials(): FinancialsRoute {
        return new FinancialsRoute();
    }

    news(): NewsRoute {
        return new NewsRoute();
    }

    financials(): FinancialsRoute {
        return new FinancialsRoute();
    }

    portfolio(): PortfolioRoute {
        return new PortfolioRoute();
    }

    price(ticker: string): PriceRoute {
        return new PriceRoute(ticker);
    }

    stocks(): StocksRoute {
        return new StocksRoute();
    }

    trades(): TradesRoute {
        return new TradesRoute();
    }

    user(): UserEndpoint {
        return new UserEndpoint();
    }

    pendingRequest<T>() {
        // eslint-disable-next-line @typescript-eslint/no-empty-function
        return new Promise<T>(() => { });
    }
}

const api = new Api();

export default api;
