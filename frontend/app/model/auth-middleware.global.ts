import { getCurrentAccount } from '~/app/api/get-current-account'
import { useCurrentAccountStore } from '~/shared/model/current-account-store'
import { useTokenCookie } from '~/shared/model/token-cookie'

export default defineNuxtRouteMiddleware(async () => {
    const token = useTokenCookie()
    const { account } = storeToRefs(useCurrentAccountStore())

    if (!account.value && token.value) {
        account.value = await getCurrentAccount()
    }
})
