import type { Question } from '~/entities/question/model/question'
import type { Survey } from '~/shared/model/survey'

export type SurveyFormData = Omit<Survey, 'questions'> & {
    questions: (Question & { id: number })[]
}
