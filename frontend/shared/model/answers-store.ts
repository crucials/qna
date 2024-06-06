export interface Answer {
    questionId: string
    answer: string | null
}

export const useAnswersStore = defineStore('answers', () => {
    const answers = ref<Answer[]>([])
    return { answers }
})
