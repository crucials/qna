<script setup lang="ts">
import { fetchApi } from '~/shared/api/fetch-api'
import authorizedOnlyMiddleware from '~/shared/model/authorized-only-middleware'
import {
    useCurrentAccountStore,
    type Account,
} from '~/shared/model/current-account-store'
import type { Survey } from '~/shared/model/survey'
import type { SurveyFormData } from '~/widgets/survey-form/model/survey-form-data'

definePageMeta({
    path: '/dashboard/surveys/create',
    middleware: authorizedOnlyMiddleware,
})

useHead({
    title: 'Create survey',
})

const { account } = storeToRefs(useCurrentAccountStore())

const newSurveyDialogData = reactive<{
    opened: boolean
    survey: Survey | null
}>({
    opened: false,
    survey: null,
})

async function createSurvey(data: SurveyFormData) {
    const questionsWithoutIds = data.questions.map((question) => ({
        ...question,
        id: undefined,
    }))

    const response = await fetchApi<Account>('/surveys', {
        method: 'POST',
        body: {
            ...data,
            questions: questionsWithoutIds,
        },
        notificationOnError: true,
    })

    const newSurvey = response.data.value?.data?.surveys.at(-1)
    if (response.data.value && newSurvey) {
        account.value = response.data.value.data
        newSurveyDialogData.survey = newSurvey
        newSurveyDialogData.opened = true
    }
}
</script>

<template>
    <h1 class="font-bold text-4xl mb-10 sm:text-3xl">Create survey</h1>

    <SurveyForm @save-survey="createSurvey" />

    <NewSurveyDialog
        :survey="newSurveyDialogData.survey"
        v-model:opened="newSurveyDialogData.opened"
    />
</template>
