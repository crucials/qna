export interface SurveyStats {
    survey_title: string
    weekly_page_visits: {
        date: Date
        count: number
    }[]
    total_visits_count: number
    responses_count: number
    responses_with_optional_question_percentage: number
}
