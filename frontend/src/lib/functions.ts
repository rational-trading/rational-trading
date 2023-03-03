export function matchAny(search: string, options: string[]): boolean {
    const searchLower = search.toLowerCase();
    return (
        options.findIndex((o) => o.toLowerCase().includes(searchLower)) !==
        -1
    );
}

export function capitalize(s: string): string {
    return s[0].toUpperCase() + s.slice(1);
}

export function convertUnixDate(unixDate: number): string {
    const date = new Date(unixDate);

    const year = `${date.getFullYear()}`;
    const month = `0${date.getMonth()}`.slice(-2);
    const day = `0${date.getDate()}`.slice(-2);

    const hour = `0${date.getHours()}`.slice(-2);
    const minute = `0${date.getMinutes()}`.slice(-2);
    const second = `0${date.getSeconds()}`.slice(-2);

    const formatedDate = `${year}-${month}-${day} ${hour}:${minute}:${second}`;
    return formatedDate;
}

export function convertValueToMoney(value: number): string {
    return `$${new Intl.NumberFormat().format(Math.round(value * 100) / 100)}`;
}

export function calculatePercentage(a: number, b: number) {
    return `${((a / b) * 100).toFixed(2)}%`;
}
