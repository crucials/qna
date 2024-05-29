import { fetchApi } from '~/shared/api/fetch-api'
import type { Account } from '~/shared/model/current-account-store'

export async function signUp(name: string, password: string) {
    const response = await fetchApi<{
        token: string
        account: Account
    }>('/auth/sign-up', {
        method: 'POST',
        body: { name, password },
        notificationOnError: true,
    })

    return response
}
