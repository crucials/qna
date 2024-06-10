<script setup lang="ts">
import type { Question } from '~/shared/model/question'
import { useAnswersStore } from '~/shared/model/answers-store'

const props = defineProps<{
    question: Question
    surveyCreationMode?: boolean
}>()

const emit = defineEmits<{
    (event: 'remove-option', option: string): void
}>()

const { answers } = storeToRefs(useAnswersStore())

const answerIndex = computed(() => {
    return answers.value.findIndex(someAnswer =>
        someAnswer.question_id === props.question._id)
})

function updateAnswer(newValue: string) {
    const answer = answers.value[answerIndex.value]

    if(answer) {
        answer.value = newValue
    }
}
</script>

<template>
    <TextField
        v-if="question.type === 'SHORT_TEXT' || question.type === 'MULTILINE_TEXT'"
        :model-value="answers[answerIndex]?.value || null"
        @update:model-value="updateAnswer"
        :disabled="surveyCreationMode"
        :multiline="question.type === 'MULTILINE_TEXT'"
        rows="6"
        :placeholder="surveyCreationMode ? 'Answer would be typed here'
            : 'Enter the answer here'"
        class="mb-7 max-w-xl"
    />

    <div
        v-if="question.type === 'ONE_OPTION' && question.options"
        class="mb-7"
    >
        <RadioButtons
            :model-value="answers[answerIndex]?.value || null"
            @update:model-value="updateAnswer"
            :options="question.options"
            :name="question.text"
            :removable-options="surveyCreationMode"
            @remove-option="option => emit('remove-option', option)"
            :disabled="surveyCreationMode"
        />
    </div>
</template>
