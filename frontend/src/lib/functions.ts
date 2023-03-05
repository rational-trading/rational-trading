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

export function convertUnixDate(unixDate: number): string {
    const date = new Date(unixDate);

    const year = `${date.getFullYear()}`;
    const month = `0${date.getMonth() + 1}`.slice(-2);
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


export function toHex<T>(object: T): string {
    return JSON.stringify(object).split("")
        .map((c) => c.charCodeAt(0).toString(16).padStart(2, "0"))
        .join("");
}

export function fromHex<T>(hex: string): T {
    return JSON.parse(hex.split(/(\w\w)/g)
        .filter((p) => !!p)
        .map((c) => String.fromCharCode(parseInt(c, 16)))
        .join(""));
}

// Adopted from https://stackblitz.com/edit/color-interpolation-multiple-colors?file=app%2Fapp.component.ts

/**
 * Interpolate two colors
 *
 * @param color1 - The starting color
 * @param color2 - The end color
 * @return The interpolated color
 */
function interpolateColor(color1: number[], color2: number[], factor = 0.5): number[] {
    const result: number[] = [];
    const factorInc = factor;

    for (let i = 0; i < color1.length; i += 1) {
        result.push(Math.round(color1[i] + factorInc * (color2[i] - color1[i])));
    }

    return result;
}

/**
 * Create an array of color values between two colors
 *
 * @param color1 - The starting color
 * @param color2 - The end color
 * @param steps - The number of desired colors
 * @return The array of color values
 */
export function interpolateColors(color1: string, color2: string, steps: number): string[] | undefined {
    if (!color1 || !color2 || !steps) {
        return;
    }
    const interpolatedColorArray: string[] = [];
    const stepFactor: number = 1 / (steps - 1);
    const color1Strings: RegExpMatchArray | null = color1.match(/\d+/g);
    const color2Strings: RegExpMatchArray | null = color2.match(/\d+/g);
    const color1Numbers: number[] | null = color1Strings ? color1Strings.map(Number) : null;
    const color2Numbers: number[] | null = color2Strings ? color2Strings.map(Number) : null;

    if (!color1Numbers || !color2Numbers) {
        return;
    }

    for (let i = 0; i < steps; i += 1) {
        const color = interpolateColor(color1Numbers, color2Numbers, stepFactor * i);
        interpolatedColorArray.push(`rgb(${color})`);
    }

    // eslint-disable-next-line consistent-return
    return interpolatedColorArray;
}
