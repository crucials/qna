export function logIn(name: string, password: string) {
    cy.session([name, password], () => {
        cy.visit('/')
        cy.contains('Log in').click({ waitForAnimations: true })
        cy.get('[data-test-id="authDialog"]').should('be.visible')

        cy.get('[data-test-id="authDialog"] input[type="text"]').type(name)
        cy.get('[data-test-id="authDialog"] input[type="password"]').type(
            password,
        )

        cy.get('[data-test-id="logInButton"]').click()
        cy.location('pathname').should('eq', '/dashboard')
    })
}
