import { getCurrentAccount } from '~/app/api/get-current-account'
import { useCurrentAccountStore } from '~/shared/model/current-account-store'

export default defineNuxtRouteMiddleware(async () => {
    const { account } = storeToRefs(useCurrentAccountStore())
    account.value = await getCurrentAccount()
})
