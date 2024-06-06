import type { Answer } from '~/shared/model/answers-store'

export interface SurveyResponseFormData {
    name: string | null
    answers: Answer[]
}
