import type { Question } from '~/entities/question/model/question'

export interface SurveyFormData {
    title: string
    anonymous: boolean
    questions: (Question & { id: number })[]
}
