const GOOGLE_AUTHORIZATION_URL = 'https://accounts.google.com/o/oauth2/v2/auth'

const AUTH_CALLBACK_ROUTE = '/auth-callback'

export function getGoogleAuthorizationUrl(clientId: string) {
    const authUrl = new URL(GOOGLE_AUTHORIZATION_URL)
    authUrl.searchParams.set('client_id', clientId)
    authUrl.searchParams.set(
        'redirect_uri',
        window.location.origin + AUTH_CALLBACK_ROUTE,
    )
    authUrl.searchParams.set('response_type', 'id_token token')
    authUrl.searchParams.set('nonce', 'sopdfgds9guy89sdfgy89d7fs')
    authUrl.searchParams.set('scope', 'email profile')
    return authUrl.toString()
}
