import { sendLogoutRequest } from '~/pages/dashboard/api/logout'
import { useCurrentAccountStore } from '~/shared/model/current-account-store'
import { useAccessTokenStore } from '~/shared/model/token-store'

export async function logout() {
    const { accessToken } = storeToRefs(useAccessTokenStore())
    const { account } = storeToRefs(useCurrentAccountStore())
    const router = useRouter()

    accessToken.value = null
    account.value = null

    await sendLogoutRequest()

    router.push('/')
}
