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
