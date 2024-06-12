import { logIn } from '../utils/log-in'

describe('create survey', () => {
    it('fill in the survey form', () => {
        logIn(Cypress.env('NEW_ACCOUNT_NAME'), Cypress.env('NEW_ACCOUNT_PASSWORD'))
        cy.visit('/#features')
    })
})
