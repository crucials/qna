import { fetchApi } from '~/shared/api/fetch-api'

export async function incrementSurveyVisitCounter(surveyId: string) {
    await fetchApi(`/surveys/${surveyId}/stats/page-visits`, {
        method: 'PUT',
    })
}
