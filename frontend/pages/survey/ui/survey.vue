<script setup lang="ts">
import { getSurveyWithQuestions } from '~/pages/survey/api/survey-with-questions'
import { fetchApi } from '~/shared/api/fetch-api';
import type { ApiError } from '~/shared/model/api-response';
import type { SurveyResponseFormData } from '~/widgets/survey-response-form/model/form-data';

definePageMeta({
    path: '/:id',
})

const id = useRoute().params.id.toString()

const { data: surveyResponse, error } = await getSurveyWithQuestions(id)

if(error.value?.statusCode === 404) {
    throw createError({
        statusCode: 404,
        message: 'Requested survey not found'
    })
}
else if(error.value) {
    throw createError({
        statusCode: 500,
        message: 'Failed to get survey data'
    })
}

useHead({
    title: surveyResponse.value?.data?.title
})

const responseSavedDialogOpened = ref(false)

async function createSurveyResponse(
    surveyResponse: SurveyResponseFormData,
    secondsSpent: number,
    setError: (error: ApiError) => void,
) {
    const apiResponse = await fetchApi(`/surveys/${id}/responses`, {
        method: 'POST',
        body: {
            name: surveyResponse.name,
            seconds_spent: secondsSpent,
            answers: surveyResponse.answers.map(answer => ({
                question_id: answer.questionId,
                value: answer.value
            }))
        },
        notificationOnError: true
    })

    if(!apiResponse.error.value) {
        responseSavedDialogOpened.value = true
    }
}
</script>

<template>
    <div v-if="surveyResponse?.data">
        <h1 class="font-bold text-4xl mb-12 lg:text-3xl">
            {{ surveyResponse.data.title }}
        </h1>

        <SurveyResponseForm
            :survey="surveyResponse.data"
            @submit-response="createSurveyResponse"
        />

        <ResponseSavedDialog v-model:opened="responseSavedDialogOpened" />
    </div>
</template>
