import type { UserSessionResponse } from '~/entities/user-session/api/user-session'
import { fetchApi } from '~/shared/api/fetch-api'

export async function logInWithGoogle(authorizationCode: string) {
    const response = await fetchApi<UserSessionResponse>(
        '/auth/log-in/google',
        {
            method: 'POST',
            body: { authorization_code: authorizationCode },
            notificationOnError: true,
            credentials: 'include',
        },
    )

    return response
}
