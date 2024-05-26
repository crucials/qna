<template>
    <div class="flex flex-col min-h-screen">
        <Header/>
        <main class="flex-grow p-6">
            <NuxtPage/>
        </main>
    </div>
</template>

<style>
@tailwind base;
@tailwind components;
@tailwind utilities;

@font-face {
    font-family: 'Inria Serif';
    src: url('~/assets/fonts/inria-serif-regular.ttf');
    font-weight: normal
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
    body {
        @apply bg-neutral-900 text-white font-libre-franklin;
    }
}
</style>
