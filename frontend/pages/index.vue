<script setup lang="ts">

</script>

<template>
    <section class="flex items-start gap-x-5 gap-y-12 justify-between flex-wrap m:gap-y-7">
        <div
            class="flex items-center gap-x-14 gap-y-7 w-full
                m:flex-col m:items-start"
        >
            <h1 class="font-bold font-inria-serif text-5xl w-2/5 m:w-full m:text-4xl">
                Ask people all over the world
            </h1>

            <div class="w-2/5 m:w-full m:hidden">
                <div class="bg-white h-1 mb-3 rounded-full w-4/5"></div>
                <div class="bg-white h-1 mb-3 rounded-full"></div>
                <div class="bg-white h-1 rounded-full w-3/4"></div>
            </div>
        </div>

        <div class="w-1/2 m:w-full">
            <p class="font-medium text-lg mb-8 max-w-lg lg:text-base">
                It’s time to move from paper and pen survey approach to
                something more comfortable. Give users awesome experience with
                beautiful customizable tests and surveys. Then, analyze answers
                in your dashboard.
            </p>

            <OutlinedButton class="mr-5">
                Start using
            </OutlinedButton>

            <FilledButton>
                Learn more
            </FilledButton>
        </div>

        <figure
            class="relative w-[38%] max-w-4xl min-w-3
                m:w-full m:max-w-xs m:order-first"
        >
            <div class="w-56 h-56 lg:w-40 lg:h-40 absolute top-1/3 left-0 bg-amethyst blur-[170px]"></div>

            <img
                class="w-full relative"
                src="~/assets/images/notebook-illustration.png"
                alt="Notebook illustration"
            />
        </figure>
    </section>
</template>

<style scoped>

</style>
