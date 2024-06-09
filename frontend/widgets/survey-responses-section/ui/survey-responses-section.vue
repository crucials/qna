<script setup lang="ts">
import {
    getSurveyResponses
} from '~/widgets/survey-responses-section/api/get-survey-responses'

const props = defineProps<{
    surveyId: string
}>()

const { data: responses, error } = await getSurveyResponses(props.surveyId)
</script>

<template>
    <section v-if="responses">
        <h2 class="text-3xl font-bold mb-5">
            Responses
        </h2>

        <p class="mb-10">
            Click on a table row to see answers
        </p>

        <div v-for="response in responses.data">
            {{ response.answers.map(answer => answer.question.text) }} -
            {{ response.seconds_spent }} seconds
        </div>
    </section>    
</template>
