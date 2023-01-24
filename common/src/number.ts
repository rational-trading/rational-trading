/**
 * Multiplies a value by 2.
 *
 * ### Example
 * ```js
 * import { double } from 'typescript-starter'
 * console.log(double(4))
 * // => 8
 * ```
 *
 * @param value - Comment describing the `value` parameter.
 * @returns Comment describing the return type.
 * @anotherNote Some other value.
 */
export const double = (value: number) => value * 2;

/**
 * Raise the value of the first parameter to the power of the second using the
 * es7 exponentiation operator (`**`).
 *
 * ### Example
 * ```ts
 * import { power } from 'typescript-starter'
 * console.log(power(2,3))
 * // => 8
 *
 * ```
 * @param base - the base to exponentiate
 * @param exponent - the power to which to raise the base
 */
export const power = (base: number, exponent: number) => base ** exponent;
