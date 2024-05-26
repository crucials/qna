/** @type {import('tailwindcss').Config} */
export default {
    content: ["./src/**/*.{js,vue,ts}"],
    theme: {
        screens: {
            '3xl': {
                min: '1750px',
            },

            '2xl': {
                max: '1400px',
            },

            xl: {
                max: '1280px',
            },

            lg: {
                max: '1050px',
            },

            m: {
                max: '768px',
            },

            sm: {
                max: '640px',
            },

            xs: {
                max: '380px',
            },
        },

        extend: {
            fontFamily: {
                graphik: 'Graphik',
            },

            minWidth: {
                1: '100px',
                1.5: '150px',
                2: '200px',
                2.5: '250px',
                3: '300px',
                3.5: '350px',
                4: '400px',
                4.5: '450px',
                5: '500px',
                5.5: '550px',
                6: '600px',
                6.5: '650px',
                7: '700px',
                7.5: '750px',
                8: '800px',
            },

            transitionProperty: {
                border: 'border-width, border-color',
                position: 'left, top, right, bottom',
                left: 'left',
                right: 'right',
                top: 'top',
                bottom: 'bottom',
            },

            minHeight: {
                1: '100px',
                1.5: '150px',
                2: '200px',
                2.5: '250px',
                3: '300px',
                3.5: '350px',
                4: '400px',
                4.5: '450px',
                5: '500px',
                5.5: '550px',
                6: '600px',
                6.5: '650px',
                7: '700px',
                7.5: '750px',
                8: '800px',
            },

            colors: {
                amethyst: {
                    DEFAULT: '#A965D7'
                }
            },

            backgroundImage: {
                'enchanted-amethyst': 'linear-gradient(90deg, rgba(169,101,215,1) 0%, rgba(80,54,242,1) 100%)',
                'silver': 'linear-gradient(90deg, rgba(64,64,64,1) 0%, rgba(104,104,104,1) 100%)',
                'chrome': ''
            },

            fontFamily: {
                'libre-franklin': 'Libre Franklin',
                'inria-serif': 'Inria Serif',
            },
        },
    },
    plugins: [],
}
