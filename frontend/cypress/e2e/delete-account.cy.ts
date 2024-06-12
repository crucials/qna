import { logIn } from '../utils/log-in'

describe('delete account', () => {
    it('send account deletion request to rest api', () => {
        logIn(Cypress.env('NEW_ACCOUNT_NAME'), Cypress.env('NEW_ACCOUNT_PASSWORD'))
        cy.getCookie('token').should('exist').then(token => {
            cy.request({
                method: 'DELETE',
                url: Cypress.env('API_BASE_URL') + '/current-account',
                headers: {
                    'Authorization': `Bearer ${token.value}`
                }
            })
        })
    })
})