<script setup lang="ts">
import type { Question } from '~/shared/model/question'
import { useForm } from '~/shared/model/form'
import { useNotificationsStore } from '~/shared/model/notifications-store'
import type { SurveyFormData } from '~/widgets/survey-form/model/survey-form-data'

const emit = defineEmits<{
    (event: 'save-survey', data: SurveyFormData): void
}>()

const { showNotification } = useNotificationsStore()
const { form, setError } = useForm<SurveyFormData>({
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

async function saveSurvey() {
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

    emit('save-survey', form.value.data)
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
            survey-creation-mode
            @update:question="newValue => updateQuestion(question.id, newValue)"
            @remove-question="form.data.questions.splice(index, 1)"
        />

        <SolidButton class="text-lg" @click="saveSurvey">
            Save survey
        </SolidButton>
    </form>
</template>
