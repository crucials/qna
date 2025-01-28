<script setup lang="ts">
import { getGoogleAuthorizationUrl } from '~/shared/api/google-oauth'

const config = useRuntimeConfig()

function redirectToGoogleAuth() {
    window.location.href = getGoogleAuthorizationUrl(
        config.public.googleOauthClientId,
    )
}
</script>

<template>
    <OutlinedButton
        color="grey"
        button-class="flex justify-center"
        @click="redirectToGoogleAuth"
    >
        Log in via Google

        <GoogleIcon class="w-6 h-6" />
    </OutlinedButton>
</template>

<style scoped></style>
