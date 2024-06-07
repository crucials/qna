<script setup lang="ts">
import authorizedOnlyMiddleware from '~/shared/model/authorized-only-middleware'
import { useCurrentAccountStore } from '~/shared/model/current-account-store'

definePageMeta({
    path: '/dashboard/surveys',
    middleware: authorizedOnlyMiddleware
})

const { account } = storeToRefs(useCurrentAccountStore())
</script>

<template>
    <h1 class="font-bold text-4xl mb-10 sm:text-3xl">
        Your surveys
    </h1>

    <div v-for="survey in account?.surveys">
        {{ survey._id }}
    </div>
</template>
