export type QuestionType = 'SHORT_TEXT' | 'MULTILINE_TEXT' | 'SINGLE_CHOICE'

export const OPTIONS_QUESTION_TYPES = ['SINGLE_CHOICE']

export interface Question {
    _id?: string
    text: string
    type: QuestionType
    options: string[] | null
    optional: boolean
}
