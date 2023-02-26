import { get } from "../request";

interface User {
    username: string;
}

interface Watchlist {
    tickers: string[];
}

interface Ticker {
    ticker: string;
}

class UserEndpoint {
    whoami(): Promise<User> {
        return get<User>({ endpoint: "/user/whoami", authenticated: true });
    }

    watchlist(): Promise<Watchlist> {
        return get<Watchlist>({ endpoint: "/user/watchlist", authenticated: true });
    }

    watchlist_add(ticker: Ticker): Promise<Ticker> {
        return get<Ticker>({ endpoint: "/user/watchlist/add", authenticated: true, queryString: `data=${ticker}` });
    }

    watchlis_remove(ticker: Ticker): Promise<Ticker> {
        return get<Ticker>({ endpoint: "/user/watchlist/remove", authenticated: true, queryString: `data=${ticker}` });
    }
}

export { UserEndpoint };
