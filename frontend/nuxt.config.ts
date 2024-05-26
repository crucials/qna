// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    devtools: { enabled: true },

    app: {
        head: {
            htmlAttrs: {
                lang: 'en',
            },
            title: 'qna',
            link: [{ rel: 'icon', type: 'image/png', href: '/favicon.png' }],
        },
    },

    srcDir: './src',

    components: [
        {
            path: '~/shared',
            pathPrefix: false,
            // Auto-import all components from shared directory.
        },

        {
            path: '~/widgets',
            pathPrefix: false,
            // Auto-import all components from shared directory.
        },

        {
            path: '~/entities',
            pathPrefix: false,
            // Auto-import all components from shared directory.
        },
    ],

    postcss: {
        plugins: {
            tailwindcss: {},
            autoprefixer: {},
        },
    },
})
