import {
    getNewAccessToken,
    refreshAccessTokenIfNeeded,
} from '~/shared/api/access-token-refresh'
import type { ApiResponse } from '~/shared/model/api-response'
import { useNotificationsStore } from '~/shared/model/notifications-store'
import { useAccessTokenStore } from '~/shared/model/token-store'

interface ApiRequestOptions {
    method?: 'GET' | 'POST' | 'DELETE' | 'PUT'
    notificationOnError?: boolean
    body?: Record<string, any>
    credentials?: 'include' | 'omit'
    headers?: HeadersInit
}

/**
 * Utility function to fetch backend API. Handles SSR,
 * auth (*inserts token in the request*) and access token refresh
 *
 * @param refreshAccessToken Flag that determines if access token must be
 * checked and refreshed if necessary before the request. `true` by default.
 * In most cases you do not need to disable it. This param is for internal use
 */
export async function fetchApi<TResponseData = null>(
    path: string,
    options?: ApiRequestOptions,
    refreshAccessToken = true,
) {
    type TypedApiResponse = ApiResponse<TResponseData>

    const config = useRuntimeConfig()
    const { accessToken } = storeToRefs(useAccessTokenStore())
    const { showNotification } = useNotificationsStore()

    if (refreshAccessToken) {
        refreshAccessTokenIfNeeded()
    }

    let response: {
        data: Ref<TypedApiResponse | null>
        error: Ref<{
            data?: TypedApiResponse
            statusCode?: number
            message?: string
        } | null>
    }

    if (process.server) {
        response = await useFetch<ApiResponse<TResponseData>>(
            config.public.apiBaseUrl + path,
            {
                headers: {
                    Authorization: 'Bearer ' + accessToken.value,
                    'Content-Type': 'application/json',
                    ...options?.headers,
                },
                method: options?.method,
                deep: false,
                body: options?.body,
                credentials: options?.credentials || 'omit',
            },
        )
    } else {
        response = await fetchOnClient(config.public.apiBaseUrl + path, {
            headers: {
                Authorization: 'Bearer ' + accessToken.value,
                'Content-Type': 'application/json',
                ...options?.headers,
            },
            method: options?.method,
            body: JSON.stringify(options?.body),
            credentials: options?.credentials || 'omit',
        })
    }

    if (response.error.value && options?.notificationOnError === true) {
        if (response.error.value.data?.error) {
            showNotification({
                type: 'error',
                message:
                    'Error: ' + response.error.value.data.error.explanation,
            })

            return response
        }

        showNotification({
            type: 'error',
            message: 'Failed to send request to the server. Try again later',
        })
    }

    return response
}

async function fetchOnClient(url: string, fetchOptions: RequestInit) {
    try {
        const clientFetchResponse = await fetch(url, fetchOptions)

        if (clientFetchResponse.ok) {
            return {
                data: ref(await clientFetchResponse.json()),
                error: ref(null),
            }
        } else {
            return {
                data: ref(null),
                error: ref({
                    data: await clientFetchResponse.json(),
                    statusCode: clientFetchResponse.status,
                }),
            }
        }
    } catch (error) {
        return {
            data: ref(null),
            error: ref({
                message: `${error}`,
            }),
        }
    }
}
