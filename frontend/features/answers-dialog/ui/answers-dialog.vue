<script setup lang="ts">
import type { Answer } from '~/shared/model/answers-store'

const props = defineProps<{
    opened: boolean
    senderName: string
    answers: Answer[]
}>()

const emit = defineEmits<{
    (event: 'update:opened', newValue: boolean): void
}>()

const answersWithQuestion = computed(
    () =>
        props.answers.filter((answer) => answer.question) as Required<Answer>[],
)
</script>

<template>
    <DialogWindow
        :opened="opened"
        @update:opened="(newValue) => emit('update:opened', newValue)"
    >
        <h2 class="font-semibold text-2xl mb-7">
            Answers from {{ senderName }}
        </h2>

        <ul>
            <QuestionCard
                v-for="(answer, index) in answersWithQuestion"
                :question="answer.question"
                :order-number="index + 1"
                tag="li"
                class="mb-6"
            />
        </ul>
    </DialogWindow>
</template>
