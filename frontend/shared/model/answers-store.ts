import type { Question } from '~/shared/model/question'

export interface Answer {
    question?: Question
    question_id: string
    value: string | null
}

export const useAnswersStore = defineStore('answers', () => {
    const answers = ref<Answer[]>([])
    return { answers }
})
