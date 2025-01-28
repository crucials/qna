<script setup lang="ts">
import { useTokenCookie } from '~/shared/model/token-cookie'

definePageMeta({
    path: '/auth-callback',
})

const route = useRoute()
const router = useRouter()

const token = useTokenCookie()

onMounted(() => {
    const googleAuthServerResponseData = new URLSearchParams(route.hash)
    const authError = googleAuthServerResponseData.get('error')
    const idToken = googleAuthServerResponseData.get('id_token')

    if (authError !== null || idToken === null) {
        console.error('Google OAuth error' + authError ? `: ${authError}` : '')

        throw createError('Log in failed')
    }

    token.value = idToken
    router.push('/dashboard')
})
</script>

<template>
    <div>
        <Spinner class="w-20 h-20 mx-auto my-20" />
    </div>
</template>

<style scoped></style>
