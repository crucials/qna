export function logIn(name: string, password: string) {
    cy.session([ name, password ], () => {
        cy.visit('/')
        cy.contains('Log in').click({ waitForAnimations: true})
        cy.get('dialog').should('be.visible')

        cy.get('dialog input[type="text"]').type(name)
        cy.get('dialog input[type="password"]').type(password)

        cy.get('dialog').contains('Log in').click()
        cy.location('pathname').should('eq', '/dashboard')
    })
}
