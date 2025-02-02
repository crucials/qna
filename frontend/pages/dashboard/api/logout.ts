import { fetchApi } from '~/shared/api/fetch-api'

export async function sendLogoutRequest() {
    return await fetchApi(
        '/auth/logout',
        { method: 'DELETE', credentials: 'include' },
        false,
    )
}
