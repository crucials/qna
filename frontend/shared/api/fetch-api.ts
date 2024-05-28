import type { ApiResponse } from '~/shared/model/api-response'
import { useNotificationsStore } from '~/shared/model/notifications-store'
import { useTokenCookie } from '~/shared/model/token-cookie'

interface ApiRequestOptions {
    method?: 'GET' | 'POST' | 'DELETE' | 'PUT'
    notificationOnError?: boolean
}

export async function fetchApi<TResponseData = null>(
    path: string, options?: ApiRequestOptions
) {
    const config = useRuntimeConfig()
    const token = useTokenCookie()
    const { showNotification } = useNotificationsStore()

    const response = await useFetch<ApiResponse<TResponseData>>(
        config.public.apiBaseUrl + path,
        {
            headers: { 'Authorization': 'Bearer ' + token.value },
            method: options?.method,
            deep: false,
        }
    )

    if(response.error.value && options?.notificationOnError === true) {
        if(response.error.value.data) {
            showNotification({
                type: 'error',
                message: 'Error: ' + response.error.value.data.error.explanation
            }, 50)

            return response
        }

        showNotification({
            type: 'error',
            message: 'Failed to send request to the server. Try again later'
        }, 50)
    }

    return response
}