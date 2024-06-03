export type QuestionType = 'SHORT_TEXT' | 'MULTILINE_TEXT' | 'ONE_OPTION'
    | 'MULTIPLE_OPTIONS'

export const OPTIONS_QUESTION_TYPES = ['MULTIPLE_OPTIONS', 'ONE_OPTION']

export interface Question {
    text: string
    type: QuestionType
    options: string[] | null
    optional: boolean
}
