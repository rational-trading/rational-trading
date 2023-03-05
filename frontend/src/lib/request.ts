import { AuthError, loadAccessToken } from "./auth";

const dev = import.meta.env.DEV;

const baseURL = dev ? "http://127.0.0.1:8000/api" : "/api";

type GetRequest = {
    type: "get",
};

type PostRequest = {
    type: "post",
    data: string
}

type Request = {
    endpoint: string, queryString?: string, authenticated?: boolean
} & (GetRequest | PostRequest);

class ApiError extends Error {
    constructor(msg: string) {
        super(msg);
        Object.setPrototypeOf(this, ApiError.prototype);
    }
}

async function request<TRes>(r: Request): Promise<TRes> {
    let response: { ok: true, value: TRes } | { ok: false, value: { error: string } };
    try {
        const res = await fetch(`${baseURL}${r.endpoint}${r.queryString ? `?${r.queryString}` : ""}`, {
            method: r.type,
            headers: r.authenticated ? { Authorization: `Bearer ${loadAccessToken()}` } : {},
            body: r.type === "post" ? r.data : undefined,
        });
        response = { ok: res.ok, value: await res.json() };
    } catch (e) {
        if (e instanceof AuthError) throw e;
        // eslint-disable-next-line no-console
        console.error(e);
        throw new ApiError("Internal server error! Check logs for details.");
    }

    if (response.ok) {
        return response.value;
    }
    throw new ApiError(response.value.error);
}

interface GetParams {
    endpoint: string,
    queryString?: string,
    authenticated?: boolean,
}

function get<TRes>({ endpoint, queryString = "", authenticated = false }: GetParams): Promise<TRes> {
    return request({
        type: "get", endpoint, queryString, authenticated,
    });
}

interface PostParams<TReq> {
    endpoint: string,
    data: TReq,
    queryString?: string,
    authenticated?: boolean,
}

function post<TReq, TRes>({
    endpoint,
    data,
    queryString = undefined,
    authenticated = false,
}: PostParams<TReq>): Promise<TRes> {
    return request({
        type: "post", endpoint, queryString, data: JSON.stringify(data), authenticated,
    });
}

export { get, post, ApiError };
