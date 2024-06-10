import { fetchApi } from '~/shared/api/fetch-api'
import type { Answer } from '~/shared/model/answers-store'

export interface SurveyResponse {
    _id: string
    name: string | null
    answers: Answer[]
    seconds_spent: number
}

export async function getSurveyResponses(surveyId: string) {
    return await fetchApi<SurveyResponse[]>(`/surveys/${surveyId}/responses`)
}
