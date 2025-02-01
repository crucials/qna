import { useCurrentAccountStore } from '~/shared/model/current-account-store'
import { useAccessTokenStore } from '~/shared/model/token-store'

export function logout() {
    const { accessToken } = storeToRefs(useAccessTokenStore())
    const { account } = storeToRefs(useCurrentAccountStore())
    const router = useRouter()

    accessToken.value = null
    account.value = null
    router.push('/')
}
