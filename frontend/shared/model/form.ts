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

    function setError(error: ApiError, removeAfterSeconds = 10) {
        form.value.error = {
            field: error.field,
            explanation: error.explanation
        }

        setTimeout(() => {
            form.value.error = null
        }, removeAfterSeconds * 1000)
    }

    return { form, setError }
}
