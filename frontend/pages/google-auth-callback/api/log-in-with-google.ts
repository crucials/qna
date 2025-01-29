import { fetchApi } from '~/shared/api/fetch-api'
import type { Account } from '~/shared/model/current-account-store'

export async function logInWithGoogle(authorizationCode: string) {
    const response = await fetchApi<{
        token: string
        account: Account
    }>('/auth/log-in/google', {
        method: 'POST',
        body: { authorization_code: authorizationCode },
        notificationOnError: true,
    })

    return response
}
