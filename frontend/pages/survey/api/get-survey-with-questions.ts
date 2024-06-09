import { fetchApi } from '~/shared/api/fetch-api'
import type { SurveyWithQuestions } from '~/shared/model/survey'

export async function getSurveyWithQuestions(id: string) {
    return await fetchApi<SurveyWithQuestions>(`/surveys/${id}`)
}
