import { getCurrentAccount } from '~/app/api/get-current-account'
import { refreshAccessTokenIfNeeded } from '~/shared/api/access-token-refresh'
import { useCurrentAccountStore } from '~/shared/model/current-account-store'
import { useAccessTokenStore } from '~/shared/model/token-store'

export default defineNuxtRouteMiddleware(async () => {
    const { accessToken } = storeToRefs(useAccessTokenStore())
    const { account } = storeToRefs(useCurrentAccountStore())

    await refreshAccessTokenIfNeeded()

    if (!account.value && accessToken.value) {
        const currentAccountResponse = await getCurrentAccount()

        if (currentAccountResponse?.data) {
            account.value = currentAccountResponse?.data
        }
    }
})
