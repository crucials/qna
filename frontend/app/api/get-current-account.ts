import type { ApiResponse } from '~/shared/model/api-response'
import type { Account } from '~/shared/model/current-account'
import { useTokenCookie } from '~/shared/model/token-cookie'

export async function getCurrentAccount() {
    const token = useTokenCookie()
    const config = useRuntimeConfig()
    
    const response = await useFetch<ApiResponse<Account>>(
        config.public.apiBaseUrl + '/auth/account',
        {
            headers: { 'Authorization': 'Bearer ' + token.value }    
        }
    )

    return response.data.value?.data || null

    /* const response1 = await $fetch<{
        data: string
    }>(config.public.apiBaseUrl + '/auth/log-in', {
        method: 'POST',
        body: {
            name: 'account_1_',
            password: '123456'
        },
    })
    
    if(response1?.data) {
        token.value = response1.data
    }

    const response = await $fetch<{
        data: Account | null
    }>(config.public.apiBaseUrl + '/auth/account', {
        headers: {
            'Authorization': 'Bearer ' + token.value
        }
    })

    return response.data */
}
