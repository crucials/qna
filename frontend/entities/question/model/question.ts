export type QuestionType = 'SHORT_TEXT' | 'MULTILINE_TEXT' | 'ONE_OPTION'

export const OPTIONS_QUESTION_TYPES = ['ONE_OPTION']

export interface Question {
    text: string
    type: QuestionType
    options: string[] | null
    optional: boolean
}
