import { get, post } from "../request";

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

    watchlist_add(ticker: Ticker): Promise<boolean> {
        return post<Ticker, boolean>({ endpoint: "/user/watchlist/add", authenticated: true, data: ticker });
    }

    watchlist_remove(ticker: Ticker): Promise<boolean> {
        return post<Ticker, boolean>({ endpoint: "/user/watchlist/remove", authenticated: true, data: ticker });
    }
}

export { UserEndpoint };
