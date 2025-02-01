import { Buffer } from 'buffer'

export const useAccessTokenStore = defineStore('access-token', () => {
    const accessToken = useCookie('token', {
        maxAge: 2592000,
    })

    function checkIfAccessTokenExpired() {
        if (!accessToken.value) {
            return false
        }

        const encodedPayload = accessToken.value.split('.')[1]

        if (encodedPayload === undefined) {
            return false
        }

        const unverifiedPayload = JSON.parse(
            Buffer.from(encodedPayload, 'base64').toString(),
        )

        return unverifiedPayload.exp * 1000 <= new Date().getTime()
    }

    return { accessToken, checkIfAccessTokenExpired }
})
