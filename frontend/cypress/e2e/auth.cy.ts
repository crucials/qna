describe('auth', () => {
    it('sign-up', () => {
        cy.session('new-account', () => {
            cy.visit('/')
            cy.contains('Log in').click({ waitForAnimations: true})
            cy.get('dialog').should('be.visible')

            cy.get('dialog input[type="text"]').type(Cypress.env('NEW_ACCOUNT_NAME'))
            cy.get('dialog input[type="password"]').type(Cypress.env('NEW_ACCOUNT_PASSWORD'))

            cy.get('dialog').contains('Sign up').click()
            cy.location('pathname').should('eq', '/dashboard')
        })
    })
})
