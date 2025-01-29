export const useAuthDialogOpenedStore = defineStore('authDialogOpened', () => {
    const authDialogOpened = ref(false)
    return { authDialogOpened }
})
