import type { Question } from '~/shared/model/question'

export interface Survey {
    _id?: string
    title: string
    anonymous: boolean
}

export type SurveyWithQuestions = Survey & { questions: Question[] }
