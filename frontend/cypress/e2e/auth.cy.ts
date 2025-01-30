describe('auth', () => {
    it('sign-up', () => {
        cy.session('new-account', () => {
            cy.visit('/')
            cy.contains('Log in').click({ waitForAnimations: true })
            cy.get('[data-test-id="authDialog"]').should('be.visible')

            cy.get('[data-test-id="authDialog"] input[type="text"]').type(
                Cypress.env('NEW_ACCOUNT_NAME'),
            )
            cy.get('[data-test-id="authDialog"] input[type="password"]').type(
                Cypress.env('NEW_ACCOUNT_PASSWORD'),
            )

            cy.get('[data-test-id="signUpButton"]').click()
            cy.location('pathname').should('eq', '/dashboard')
        })
    })
})
