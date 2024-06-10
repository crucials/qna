import type { AnswerWithQuestion } from '~/entities/answers-dialog/model/answer-with-question'
import { fetchApi } from '~/shared/api/fetch-api'

export interface SurveyResponse {
    _id: string
    name: string | null
    answers: AnswerWithQuestion[]
    seconds_spent: number
}

export async function getSurveyResponses(surveyId: string) {
    return await fetchApi<SurveyResponse[]>(`/surveys/${surveyId}/responses`)
}
