export function useTokenCookie() {
    const token = useCookie('token', {
        maxAge: 2592000,
    })

    return token
}
