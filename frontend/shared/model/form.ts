import type { ApiError } from '~/shared/model/api-response'

export function useForm<TFormData extends Object>(initialValue: TFormData) {
    const form = ref<{
        data: TFormData
        error: {
            field?: string
            explanation: string
        } | null
    }>({
        data: initialValue,
        error: null
    })

    let lastErrorTimeoutId: number | undefined = undefined
    function setError(error: ApiError, removeAfterSeconds = 7) {
        form.value.error = {
            field: error.field,
            explanation: error.explanation
        }

        window.clearTimeout(lastErrorTimeoutId)
        
        lastErrorTimeoutId = window.setTimeout(() => {
            form.value.error = null
        }, removeAfterSeconds * 1000)
    }

    return { form, setError }
}
