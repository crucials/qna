import { logIn } from '../utils/log-in'

let newSurveyUrl: string | undefined = undefined

describe('surveys', () => {
    it('create survey', () => {
        logIn(Cypress.env('NEW_ACCOUNT_NAME'), Cypress.env('NEW_ACCOUNT_PASSWORD'))

        cy.visit('/dashboard/surveys/create')

        cy.intercept(Cypress.env('FRONTEND_URL') + '/_nuxt/*/**').as('hydration')
        cy.wait('@hydration')

        cy.get('input[placeholder="Enter the survey title"]').type('test survey', {
            delay: 300,
            release: false
        })

        // opening create question menu and choosing short text question
        cy.get('form button[aria-haspopup="listbox"]').click()
        cy.get('form ul[role="listbox"]').should('be.visible')
            .contains('Short text').click()
        
        cy.get('input[placeholder="Enter the question text"]').type('test question 1')
        
        // creating radio buttons question
        cy.get('form button[aria-haspopup="listbox"]').click()
        cy.get('form ul[role="listbox"]').should('be.visible')
            .contains('One option').click()      
        
        cy.get('input[placeholder="Enter the question text').eq(1).type('test question 2')
        cy.get('input[placeholder="Option name"]').type('option 1')
        cy.contains('Add option').click()

        cy.get('input[placeholder="Option name"]').type('option 2')
        cy.contains('Add option').click()

        cy.contains('Save survey').click()

        cy.get('dialog button[title="Copy"]').then(copyUrlButton => {
            newSurveyUrl = copyUrlButton.text()
        })
    })
})
