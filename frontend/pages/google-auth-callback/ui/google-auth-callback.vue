<script setup lang="ts">
import { useCurrentAccountStore } from '~/shared/model/current-account-store'
import { logInWithGoogle } from '../api/log-in-with-google'
import { useNotificationsStore } from '~/shared/model/notifications-store'
import { useAccessTokenStore } from '~/shared/model/token-store'

definePageMeta({
    path: '/auth-callback',
})

const route = useRoute()
const router = useRouter()

const { showNotification } = useNotificationsStore()

const { accessToken } = storeToRefs(useAccessTokenStore())
const { account } = storeToRefs(useCurrentAccountStore())

onMounted(async () => {
    const authError = route.query.error
    const code = route.query.code

    if (authError || !code) {
        console.error('Google OAuth error' + authError ? `: ${authError}` : '')

        throw createError('Log in failed')
    }

    const googleLogInResponse = (await logInWithGoogle(code.toString())).data
        .value

    if (!googleLogInResponse?.data?.access_token) {
        console.error(
            'Auth error:',
            googleLogInResponse?.error?.explanation ||
                'Token is missing in response body',
        )

        throw createError('Log in failed')
    }

    accessToken.value = googleLogInResponse.data.access_token
    account.value = googleLogInResponse.data.account

    showNotification({ message: 'Logged in', type: 'success' })
    router.push('/dashboard')
})
</script>

<template>
    <div>
        <Spinner class="w-20 h-20 mx-auto my-20" />
    </div>
</template>

<style scoped></style>
