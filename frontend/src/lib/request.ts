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
    endpoint: string, queryString?: string, bearer?: string
} & (GetRequest | PostRequest);

class ApiError extends Error {
    constructor(msg: string) {
        super(msg);

        // Set the prototype explicitly.
        Object.setPrototypeOf(this, ApiError.prototype);
    }
}

async function request<TRes>(r: Request): Promise<TRes> {
    let response: { ok: true, value: TRes } | { ok: false, value: {error: string} };
    try {
        const res = await fetch(`${baseURL}${r.endpoint}${r.queryString ? `?${r.queryString}` : ""}`, {
            method: r.type,
            headers: r.bearer ? { Authorization: `Bearer ${r.bearer}` } : {},
            body: r.type === "post" ? r.data : undefined,
        });
        response = { ok: res.ok, value: await res.json() };
    } catch (e) {
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
    bearer?: string,
}

function get<TRes>({ endpoint, queryString = "", bearer = undefined }: GetParams): Promise<TRes> {
    return request({
        type: "get", endpoint, queryString, bearer,
    });
}

interface PostParams<TReq> {
    endpoint: string,
    data: TReq,
    queryString?: string,
    bearer?: string,
}

function post<TReq, TRes>({
    endpoint,
    data,
    queryString = undefined,
    bearer = undefined,
}: PostParams<TReq>): Promise<TRes> {
    return request({
        type: "post", endpoint, queryString, data: JSON.stringify(data), bearer,
    });
}

export { get, post };
