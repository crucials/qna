<script setup lang="ts">
import type { Question } from '~/entities/question/model/question'

withDefaults(defineProps<{
    question: Question
    orderNumber?: number
    tag?: string
}>(), { tag: 'li' })

const emit = defineEmits<{
    (event: 'update:question', newValue: Question): void
}>()

const answer = ref('')
</script>

<template>
    <component :is="tag" class="max-w-3xl">
        <div
            class="text-amethyst mb-0.5"
            v-if="orderNumber"
        >
            Question {{ orderNumber }}
        </div>

        <TextField
            :model-value="question.text"
            @update:model-value="newValue => emit('update:question', {
                ...question,
                text: newValue
            })"
            underlined
            placeholder="Enter the question title"
            class="mb-6"
        />

        <TextField
            v-model="answer"
            disabled
            placeholder="Answer would be typed here"
            class="mb-6"
        />

        <ToggleInput
            :model-value="question.optional"
            @update:model-value="newValue => emit('update:question', {
                ...question,
                optional: newValue
            })"
        >
            Optional
        </ToggleInput>
    </component>
</template>
