import type { Account } from '~/shared/model/current-account-store'

export interface UserSessionResponse {
    access_token: string
    account: Account
}
