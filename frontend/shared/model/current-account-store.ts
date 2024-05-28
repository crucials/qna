export interface Account {
    name: string
}

export const useCurrentAccountStore = defineStore('account', () => {
    const account = ref<Account | null>(null)

    return { account }
})
