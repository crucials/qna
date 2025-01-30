import dotenv from 'dotenv'
import { defineConfig } from 'cypress'

dotenv.config()

export default defineConfig({
    env: {
        ...process.env,
        NEW_ACCOUNT_NAME: `account_${crypto.randomUUID().slice(0, 6)}`,
        NEW_ACCOUNT_PASSWORD: '123456',
    },

    requestTimeout: 2000,
    defaultCommandTimeout: 5000,
    retries: 3,

    e2e: {
        setupNodeEvents(on, config) {
            // implement node event listeners here
        },
        baseUrl: process.env.FRONTEND_URL,
        specPattern: [
            'cypress/e2e/auth.cy.ts',
            'cypress/e2e/surveys.cy.ts',
            'cypress/e2e/delete-account.cy.ts',
        ],
    },
})
