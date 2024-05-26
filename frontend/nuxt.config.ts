// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    devtools: { enabled: true },

    modules: [ '@vueuse/nuxt' ],

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
            path: '~/shared',
            pathPrefix: false,
        },

        {
            path: '~/widgets',
            pathPrefix: false,
        },

        {
            path: '~/entities',
            pathPrefix: false,
        },
    ],

    postcss: {
        plugins: {
            tailwindcss: {},
            autoprefixer: {},
        },
    },
})
