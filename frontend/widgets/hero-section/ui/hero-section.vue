<script setup lang="ts">
const mounted = useMounted()
</script>

<template>
    <section
        class="flex items-start gap-x-5 gap-y-12 justify-between flex-wrap
            m:gap-y-7"
    >
        <div
            class="flex items-center gap-x-8 gap-y-7 w-full
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

            <div class="flex gap-5 flex-wrap">
                <OutlinedButton>
                    Start using
                </OutlinedButton>

                <FilledButton tag="a" href="#features">
                    Learn more
                </FilledButton>
            </div>
        </div>

        <figure
            class="relative w-[38%] max-w-4xl min-w-3
                m:w-full m:max-w-xs m:order-first"
        >
            <!-- lighting -->
            <div
                class="w-56 h-56 absolute top-1/3 left-0
                    bg-amethyst blur-[170px] lg:w-40 lg:h-40"
            ></div>

            <img
                class="w-full relative transition-all duration-700"
                :class="{ 'opacity-0 translate-x-32 blur-sm': !mounted }"
                src="~/assets/images/notebook-illustration.png"
                alt="Notebook illustration"
            />
        </figure>
    </section>    
</template>
