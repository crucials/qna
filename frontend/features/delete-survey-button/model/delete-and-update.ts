import { deleteSurvey } from '~/features/delete-survey-button/api/delete'
import { useCurrentAccountStore } from '~/shared/model/current-account-store'

export async function deleteSurveyAndUpdate(id: string) {
    const { account } = storeToRefs(useCurrentAccountStore())

    if (account.value) {
        account.value.surveys = account.value.surveys.filter(
            (survey) => survey._id !== id,
        )
    }

    await deleteSurvey(id)
}
