<script setup lang="ts">
import { getSurveyWithQuestions } from '~/pages/survey/api/survey-with-questions'
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

async function createSurveyResponse(
    response: SurveyResponseFormData,
    setError: (error: ApiError) => void
) {
    
}
</script>

<template>
    <div v-if="surveyResponse?.data">
        <h1 class="font-bold text-4xl mb-12 lg:text-3xl">
            {{ surveyResponse.data.title }}
        </h1>

        <SurveyResponseForm
            :survey="surveyResponse.data"
        />
    </div>
</template>
