export interface Activity {
    time: string;
    symbol: string;
    quantity_bought: number;
    price: number;
    status: "Filled" | "Pending" | "Rejected";
}
