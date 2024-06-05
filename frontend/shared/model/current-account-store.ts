import type { Survey } from '~/shared/model/survey'

export interface Account {
    name: string
    surveys: Survey[]
}

export const useCurrentAccountStore = defineStore('account', () => {
    const account = ref<Account | null>(null)

    return { account }
})
