import type { Question } from '~/entities/question/model/question'
import { fetchApi } from '~/shared/api/fetch-api'
import type { Survey } from '~/shared/model/survey'

export type SurveyWithQuestions = Survey & { questions: Question[] }

export async function getSurveyWithQuestions(id: string) {
    return await fetchApi<SurveyWithQuestions>(`/surveys/${id}`)
}
