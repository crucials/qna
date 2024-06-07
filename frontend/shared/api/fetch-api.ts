import type { ApiResponse } from '~/shared/model/api-response'
import { useNotificationsStore } from '~/shared/model/notifications-store'
import { useTokenCookie } from '~/shared/model/token-cookie'

interface ApiRequestOptions {
    method?: 'GET' | 'POST' | 'DELETE' | 'PUT'
    notificationOnError?: boolean
    body?: Record<string, any>
}

export async function fetchApi<TResponseData = null>(
    path: string, options?: ApiRequestOptions
) {
    type TypedApiResponse = ApiResponse<TResponseData>

    const config = useRuntimeConfig()
    const token = useTokenCookie()
    const { showNotification } = useNotificationsStore()

    let response: {
        data: Ref<TypedApiResponse | null>
        error: Ref<{
            data?: TypedApiResponse
            statusCode?: number
            message?: string
        } | null>
    }

    if(process.server) {
        response = await useFetch<ApiResponse<TResponseData>>(
            config.public.apiBaseUrl + path,
            {
                headers: { 'Authorization': 'Bearer ' + token.value },
                method: options?.method,
                deep: false,
                body: options?.body
            }
        )
    }
    else {
        response = await fetchOnClient(config.public.apiBaseUrl + path, {
            headers: { 'Authorization': 'Bearer ' + token.value },
            method: options?.method,
            body: JSON.stringify(options?.body)
        })
    }

    if(response.error.value && options?.notificationOnError === true) {
        if(response.error.value.data?.error) {
            showNotification({
                type: 'error',
                message: 'Error: ' + response.error.value.data.error.explanation
            })

            return response
        }

        showNotification({
            type: 'error',
            message: 'Failed to send request to the server. Try again later'
        })
    }

    return response
}

async function fetchOnClient(url: string, fetchOptions: RequestInit) {
    try {
        const clientFetchResponse = await fetch(url, fetchOptions)

        if(clientFetchResponse.ok) {
            return {
                data: ref(await clientFetchResponse.json()),
                error: ref(null)
            }
        }
        else {
            return {
                data: ref(null),
                error: ref({
                    data: await clientFetchResponse.json(),
                    statusCode: clientFetchResponse.status
                })
            }
        }
    }
    catch(error) {
        return {
            data: ref(null),
            error: ref({
                message: `${error}`
            })
        }
    }
}
