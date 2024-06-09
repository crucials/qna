import type { SurveyStats } from '~/entities/survey-stats/model/survey-stats'
import { fetchApi } from '~/shared/api/fetch-api'

export async function getSurveyStats(surveyId: string) {
    return await fetchApi<SurveyStats>(`/surveys/${surveyId}/stats`)
}
