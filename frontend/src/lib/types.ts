export interface Activity {
    time: number;
    symbol: string;
    quantity_bought: number;
    price: number;
    status: "Filled" | "Pending" | "Rejected";
}

export interface News {
    title: string;
    publisher: string;
    published_utc: string;
    description: string;
    url: string;
    sentiment: boolean;
}

export interface Stock {
    ticker: string;
    name: string;
    exchange: string;
}

export interface TokenSchema {
    access_token: string;
}
