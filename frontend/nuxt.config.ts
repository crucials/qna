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

    components: [
        {
            path: '~/components',
            pathPrefix: false
        }
    ],

    postcss: {
        plugins: {
            tailwindcss: {},
            autoprefixer: {},
        },
    },
})
