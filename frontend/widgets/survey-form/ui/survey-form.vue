<script setup lang="ts">
import type { Question } from '~/entities/question/model/question'
import { useForm } from '~/shared/model/form'

const { form, setError } = useForm<{
    title: string
    anonymous: boolean
    questions: Question[]
}>({
    title: '',
    anonymous: false,
    questions: []
})
</script>

<template>
    <form>
        <div class="flex items-center gap-x-12 gap-y-6 lg:flex-wrap mb-20">
            <TextField
                v-model="form.data.title"
                placeholder="Enter the survey title"
                underlined
                class="text-2xl lg:text-xl sm:text-lg"
                wrapper-class="w-1/2 min-w-4 sm:w-full sm:min-w-2.5"
                :error="form.error?.field === 'title'"
            />

            <ToggleInput v-model="form.data.anonymous">
               Anonymous 
            </ToggleInput>
            
            <CreateQuestionMenu
                @create-question="question => form.data.questions.push(question)"
            />
        </div>

        <ul>
            <QuestionCard
                v-for="question, index in form.data.questions"
                v-model:question="form.data.questions[index]"
                :order-number="index + 1"
                class="mb-14 last-of-type:mb-0"
            />
        </ul>
    </form>
</template>
