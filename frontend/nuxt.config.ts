// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    devtools: { enabled: true },

    modules: [
        '@vueuse/nuxt',

        [
            '@pinia/nuxt',
            {
                autoImports: [
                    'defineStore', 'storeToRefs'
                ]
            }
        ]
    ],
    postcss: {
        plugins: {
            tailwindcss: {},
            autoprefixer: {},
        },
    },

    dir: {
        'middleware': 'app/*'
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

        {
            path: '~/features',
            pathPrefix: false,
        },
    ],

    app: {
        head: {
            htmlAttrs: {
                lang: 'en',
            },
            title: 'qna',
            link: [{ rel: 'icon', type: 'image/png', href: '/favicon.png' }],
        },
    },

    runtimeConfig: {
        public: {
            apiBaseUrl: process.env.API_BASE_URL,
        }
    }
})
