export interface ApiError {
    code: number
    explanation: string
    field?: string
}

export type ApiResponse<TData = null> = {
    data: TData | null
    error: ApiError | null
}
