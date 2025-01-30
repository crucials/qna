import { fetchApi } from '~/shared/api/fetch-api'

export async function deleteSurvey(id: string) {
    await fetchApi(`/surveys/${id}`, {
        method: 'DELETE',
        notificationOnError: true,
    })
}
