<script setup lang="ts">
import { fetchApi } from '~/shared/api/fetch-api'
import authorizedOnlyMiddleware from '~/shared/model/authorized-only-middleware'
import type { Account } from '~/shared/model/current-account-store'
import type { SurveyFormData } from '~/widgets/survey-form/model/survey-form-data'

definePageMeta({
    path: '/surveys/create',
    middleware: authorizedOnlyMiddleware
})

async function createSurvey(data: SurveyFormData) {
    const questionsWithoutIds = data.questions.map(question => ({
        ...question,
        id: undefined
    }))

    const response = await fetchApi<Account>('/current-account/surveys', {
        method: 'POST',
        body: {
            ...data,
            questions: questionsWithoutIds,
        },
        notificationOnError: true
    })
}
</script>

<template>
    <h1 class="font-bold text-4xl mb-10 sm:text-3xl">
        Create survey
    </h1>

    <SurveyForm @save-survey="createSurvey" />
</template>
