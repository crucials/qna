<script setup lang="ts">
import type { Question } from '~/entities/question/model/question'

defineProps<{
    question: Question
    modelValue?: string
    removableOptions?: boolean
    disabled?: boolean
}>()

const emit = defineEmits<{
    (event: 'remove-option', option: string): void
}>()

const answer = ref('')
</script>

<template>
    <TextField
        v-if="question.type === 'SHORT_TEXT' || question.type === 'MULTILINE_TEXT'"
        v-model="answer"
        :disabled="disabled"
        :multiline="question.type === 'MULTILINE_TEXT'"
        rows="6"
        placeholder="Answer would be typed here"
        class="mb-7"
    />

    <div
        v-if="question.type === 'ONE_OPTION' && question.options"
        class="mb-7"
    >
        <RadioButtons
            v-model="answer"
            :options="question.options"
            :name="question.text"
            :removable-options="removableOptions"
            @remove-option="option => emit('remove-option', option)"
            disabled
            class="mb-6"
        />
    </div>
</template>
