export interface Answer {
    questionId: string
    value: string | null
}

export const useAnswersStore = defineStore('answers', () => {
    const answers = ref<Answer[]>([])
    return { answers }
})
