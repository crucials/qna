import type { Account } from '~/shared/model/current-account'

export async function getCurrentAccount() {
    const config = useRuntimeConfig()
    const response1 = await $fetch(config.public.apiBaseUrl + '/auth/log-in', {
        method: 'POST',
        body: {
            name: 'account_1_',
            password: '123456'
        },
        credentials: 'include',
    })
    console.log(response1)

    const response = await $fetch<{
        data: Account | null
    }>(config.public.apiBaseUrl + '/auth/account')

    return response.data
}
