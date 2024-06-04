<script setup lang="ts">
import type { Question } from '~/entities/question/model/question'
import { fetchApi } from '~/shared/api/fetch-api';
import { useForm } from '~/shared/model/form'
import { useNotificationsStore } from '~/shared/model/notifications-store'

const { showNotification } = useNotificationsStore()
const { form, setError } = useForm<{
    title: string
    anonymous: boolean
    questions: (Question & { id: number })[]
}>({
    title: '',
    anonymous: false,
    questions: []
})

let lastQuestionId = 0
function addQuestion(question: Question) {
    form.value.data.questions.push({
        ...question,
        id: lastQuestionId
    })

    lastQuestionId++
}

function updateQuestion(questionId: number, newValue: Question) {
    const index = form.value.data.questions
        .findIndex(question => question.id === questionId)
    
    form.value.data.questions[index] = {
        id: questionId,
        ...newValue
    }
}

async function createSurvey() {
    if(form.value.data.title.length < 3) {
        setError({
            field: 'title',
            explanation: 'Survey title must be minimum of 3 chars long'
        })
        showNotification({
            type: 'error',
            message: 'Survey title must be minimum of 3 chars long'
        })
        return
    }

    if(form.value.data.questions.length === 0) {
        showNotification({
            type: 'error',
            message: 'Add at least one question'
        })
        return
    }

    const response = await fetchApi('/current-account/surveys', {
        method: 'POST',
        body: form.value.data,
        notificationOnError: true
    })
}
</script>

<template>
    <form>
        <div class="flex items-center gap-x-12 gap-y-6 lg:flex-wrap mb-20">
            <TextField
                v-model.trim="form.data.title"
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
                @create-question="addQuestion"
            />
        </div>

        <QuestionCard
            v-for="question, index in form.data.questions"
            :key="index"
            :question="question"
            :order-number="index + 1"
            class="mb-16"
            tag="fieldset"
            @update:question="newValue => updateQuestion(question.id, newValue)"
            @remove-question="form.data.questions.splice(index, 1)"
        />

        <SolidButton class="text-lg" @click="createSurvey">
            Create survey
        </SolidButton>
    </form>
</template>
