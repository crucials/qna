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
    <div v-if="account">
        <h1 class="font-bold text-4xl mb-10 sm:text-3xl">
            Your surveys
        </h1>

        <ul class="flex gap-6 flex-wrap">
            <SurveyCard
                v-for="survey in account.surveys"
                :key="survey._id"
                :survey="survey"
                class="w-1/5"
            />
        </ul>
    </div>
</template>
