import { fetchApi } from '~/shared/api/fetch-api'
import type { Account } from '~/shared/model/current-account-store'

export async function getCurrentAccount() {
    const response = await fetchApi<Account>('/current-account')
    return response.data.value
}
