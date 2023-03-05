import api from "./api";
import { user } from "./stores";


class AuthError extends Error {
    constructor(msg: string) {
        super(msg);
        Object.setPrototypeOf(this, AuthError.prototype);
    }
}


async function logout() {
    localStorage.removeItem("access_token");
    user.set(false);
}

/**
 * Sets the access token if provided (otherwise uses the existing one, if it exists)
 * and attempts to refresh the `user` store.
 * @param token Bearer token retrieved through login or signup.
 * @throws {AuthError} if token (either provided or loaded) is invalid.
 */
async function authenticate(token: string | null = null) {
    if (token) {
        localStorage.setItem("access_token", token);
    }
    try {
        user.set(await api.user().whoami());
    } catch {
        user.set(false);
        throw new AuthError("Invalid access token!");
    }
}


/**
 * Retrieves the access token from localstorage.
 * @throws {AuthError} if token does not exist.
 * @returns
 */
function loadAccessToken(): string {
    const token = localStorage.getItem("access_token");
    if (token) return token;
    throw new AuthError("Not authenticated!");
}


export {
    authenticate, loadAccessToken, AuthError, logout,
};
