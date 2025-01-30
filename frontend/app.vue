<template>
    <RootLayout>
        <NuxtPage />
    </RootLayout>
</template>

<style>
@tailwind base;
@tailwind components;
@tailwind utilities;

@font-face {
    font-family: 'Inria Serif';
    src: url('~/assets/fonts/inria-serif-regular.ttf');
    font-weight: normal;
}

@font-face {
    font-family: 'Inria Serif';
    src: url('~/assets/fonts/inria-serif-light.ttf');
    font-weight: 300;
}

@font-face {
    font-family: 'Inria Serif';
    src: url('~/assets/fonts/inria-serif-bold.ttf');
    font-weight: 700;
}

@font-face {
    font-family: 'Libre Franklin';
    src: url('~/assets/fonts/libre-franklin.ttf');
}

@layer base {
    html {
        @apply scroll-smooth;
    }

    body {
        @apply bg-[#0E0E0E] text-white font-libre-franklin;
    }

    * {
        @apply focus-visible:outline-none focus-visible:ring-4
            focus-visible:ring-amethyst/40;
    }
}
</style>
