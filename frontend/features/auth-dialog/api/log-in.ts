import { fetchApi } from '~/shared/api/fetch-api'

export async function logInForToken(name: string, password: string) {
    const response = await fetchApi<string>('/auth/log-in', {
        method: 'POST',
        body: { name, password },
        notificationOnError: true,
    })

    return response
}
