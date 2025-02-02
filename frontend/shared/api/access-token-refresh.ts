import { fetchApi } from '~/shared/api/fetch-api'
import { useAccessTokenStore } from '~/shared/model/token-store'

export async function getNewAccessToken() {
    const isServerSide = process.server
    const refreshToken = useCookie('refresh-token')

    const accessTokenResponse = await fetchApi(
        '/auth/access-token',
        {
            method: 'POST',
            credentials: 'include',
            headers: isServerSide
                ? { Cookie: 'refresh-token=' + refreshToken.value }
                : {},
        },
        false,
    )

    return accessTokenResponse.data.value?.data
}

export async function refreshAccessTokenIfNeeded() {
    const accessTokenStore = useAccessTokenStore()

    if (accessTokenStore.checkIfAccessTokenExpired()) {
        const newAccessToken = await getNewAccessToken()

        if (newAccessToken) {
            accessTokenStore.accessToken = newAccessToken
        } else {
            console.error(
                'Failed to refresh the token, perhaps the session is expired',
            )
        }
    }
}
