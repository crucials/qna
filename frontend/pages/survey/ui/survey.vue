<script setup lang="ts">
import { getSurveyWithQuestions } from '~/pages/survey/api/survey-with-questions'

definePageMeta({
    path: '/surveys/:id',
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
