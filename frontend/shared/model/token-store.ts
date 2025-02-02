import { Buffer } from 'buffer'

export const useAccessTokenStore = defineStore('access-token', () => {
    const accessToken = useCookie('token', {
        maxAge: 2592000,
    })

    const accessTokenExpirationTimestamp = computed(() => {
        if (!accessToken.value) {
            return undefined
        }

        const encodedPayload = accessToken.value.split('.')[1]

        if (encodedPayload === undefined) {
            return undefined
        }

        const unverifiedPayload = JSON.parse(
            Buffer.from(encodedPayload, 'base64').toString(),
        )

        return unverifiedPayload.exp * 1000
    })

    function checkIfAccessTokenExpired() {
        if (accessTokenExpirationTimestamp.value === undefined) {
            return false
        }

        return (
            accessTokenExpirationTimestamp.value <= new Date().getTime()
        )
    }

    return { accessToken, checkIfAccessTokenExpired, accessTokenExpirationTimestamp }
})
