import type { UserSessionResponse } from '~/entities/user-session/api/user-session'
import { fetchApi } from '~/shared/api/fetch-api'

export async function logIn(name: string, password: string) {
    const response = await fetchApi<UserSessionResponse>('/auth/log-in', {
        method: 'POST',
        body: { name, password },
        notificationOnError: true,
        credentials: 'include',
    })

    return response
}
