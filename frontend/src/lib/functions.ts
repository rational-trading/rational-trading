export function matchAny(search: string, options: string[]): boolean {
    const searchLower = search.toLowerCase();
    return (
        options.findIndex((o) => o.toLowerCase().includes(searchLower)) !==
        -1
    );
}

export function howLongAgo(time: string): string {
    const hours = Math.round(((new Date()).valueOf() - (new Date(time)).valueOf()) / 3600000);

    if (hours === 0) {
        return "Just now";
    }

    if (hours < 24) {
        if (hours === 1) {
            return "1 hour ago";
        }
        return `${hours} hours ago`;
    }

    const days = Math.round(hours / 24);
    if (days < 7) {
        if (days === 1) {
            return "1 day ago";
        }
        return `${days} days ago`;
    }

    const weeks = Math.round(days / 7);
    if (weeks === 1) {
        return "1 week ago";
    }
    return `${weeks} weeks ago`;
}
