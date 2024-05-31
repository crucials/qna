import { useCurrentAccountStore } from '~/shared/model/current-account-store'

export default defineNuxtRouteMiddleware(async () => {
    const { account } = storeToRefs(useCurrentAccountStore())

    if(!account.value) {
        return await navigateTo('/')
    }
})
