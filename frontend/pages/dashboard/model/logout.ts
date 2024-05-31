import { useCurrentAccountStore } from '~/shared/model/current-account-store'
import { useTokenCookie } from '~/shared/model/token-cookie'

export function logout() {
    const token = useTokenCookie()
    const { account } = storeToRefs(useCurrentAccountStore())
    const router = useRouter()

    token.value = null
    account.value = null
    router.push('/')
}
