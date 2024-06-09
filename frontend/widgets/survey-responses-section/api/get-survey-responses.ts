import { fetchApi } from '~/shared/api/fetch-api'
import type { Answer } from '~/shared/model/answers-store'
import type { Question } from '~/shared/model/question'

export type AnswerWithQuestion = Answer & { question: Question }

export interface SurveyResponse {
    _id: string
    name: string | null
    answers: AnswerWithQuestion[]
    seconds_spent: number
}

export async function getSurveyResponses(surveyId: string) {
    return await fetchApi<SurveyResponse[]>(`/surveys/${surveyId}/responses`)
}
