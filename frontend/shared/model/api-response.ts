export type ApiResponse<TData = null> = {
    data: TData | null
    error: {
        code: number
        explanation: string
        invalidField?: string
    } | null
}
