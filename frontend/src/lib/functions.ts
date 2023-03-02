import TimeAgo from "javascript-time-ago";
import en from "javascript-time-ago/locale/en";

TimeAgo.addDefaultLocale(en);


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

export function timeAgo(datetime: Date): string {
    return new TimeAgo("en-US").format(datetime);
}

export function toHex<T>(object: T): string {
    return JSON.stringify(object).split("")
        .map((c) => c.charCodeAt(0).toString(16).padStart(2, "0"))
        .join("");
}

export function fromHex<T>(hex: string): T {
    return JSON.parse(hex.split("")
        .map((c) => c.charCodeAt(0).toString(16).padStart(2, "0"))
        .join(""));
}
