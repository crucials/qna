<template>
    <section class="relative min-h-7.5">
        <div class="circle-grid-background-decoration left"></div>
        <div class="circle-grid-background-decoration right"></div>
        <div class="circle-grid-background-decoration bottom"></div>

        <h2
            class="font-inria-serif font-bold text-4xl text-center mb-14
                sm:mb-8 m:text-3xl"
        >
            Why you should try
            <span class="text-amethyst">qna</span>
        </h2>

        <ul
            class="grid grid-cols-2 gap-7 w-3/4 mx-auto pt-8
                xl:w-11/12 m:grid-cols-1 xs:pt-0"
        >
            <FeatureCard
                class="-translate-x-8 -translate-y-8 xs:transform-none"
                title="Attractive UI"
                description="Make users more interested in your survey with modern
                    UI an UX design."
            >
                <template #icon>
                    <svg
                        class="flex-shrink-0 w-20 lg:w-16"
                        viewBox="0 0 84 84"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <path
                            d="M70.875 10.5H13.125C8.6625 10.5 5.25 13.9125 5.25 18.375V65.625C5.25 70.0875 8.6625 73.5 13.125 73.5H70.875C75.3375 73.5 78.75 70.0875 78.75 65.625V18.375C78.75 13.9125 75.3375 10.5 70.875 10.5ZM31.7625 19.95C32.025 19.6875 32.025 19.425 32.2875 19.1625C33.3375 18.1125 34.9125 18.1125 35.9625 19.1625C36.225 19.425 36.4875 19.6875 36.4875 19.95C36.75 20.2125 36.75 20.7375 36.75 21C36.75 21.2625 36.75 21.7875 36.4875 22.05C36.225 22.3125 36.225 22.575 35.9625 22.8375C35.4375 23.3625 34.9125 23.625 34.125 23.625C33.8625 23.625 33.3375 23.625 33.075 23.3625C32.8125 23.1 32.55 23.1 32.2875 22.8375C32.025 22.575 31.7625 22.3125 31.7625 22.05C31.5 21.7875 31.5 21.2625 31.5 21C31.5 20.7375 31.5 20.2125 31.7625 19.95ZM23.8875 19.95C24.15 19.6875 24.15 19.425 24.4125 19.1625C24.675 18.9 24.9375 18.6375 25.2 18.6375C26.25 18.1125 27.3 18.375 28.0875 19.1625C28.35 19.425 28.6125 19.6875 28.6125 19.95C28.875 20.2125 28.875 20.7375 28.875 21C28.875 21.7875 28.6125 22.3125 28.0875 22.8375C27.5625 23.3625 27.0375 23.625 26.25 23.625C25.4625 23.625 24.9375 23.3625 24.4125 22.8375C23.8875 22.3125 23.625 21.7875 23.625 21C23.625 20.7375 23.625 20.2125 23.8875 19.95ZM16.5375 19.1625L16.8 18.9C17.0625 18.9 17.0625 18.6375 17.325 18.6375C17.5875 18.375 17.5875 18.375 17.85 18.375C18.1125 18.375 18.6375 18.375 18.9 18.375C19.1625 18.375 19.1625 18.375 19.425 18.6375C19.6875 18.6375 19.6875 18.9 19.95 18.9L20.2125 19.1625C20.475 19.425 20.7375 19.6875 20.7375 19.95C21 20.2125 21 20.7375 21 21C21 21.2625 21 21.7875 20.7375 22.05C20.7375 22.3125 20.475 22.575 20.2125 22.8375C19.6875 23.3625 19.1625 23.625 18.375 23.625C17.5875 23.625 17.0625 23.3625 16.5375 22.8375C16.0125 22.3125 15.75 21.7875 15.75 21C15.75 20.2125 16.0125 19.6875 16.5375 19.1625ZM47.25 68.25H13.125C11.55 68.25 10.5 67.2 10.5 65.625V52.5H47.25V68.25ZM47.25 47.25H10.5V31.5H47.25V47.25ZM73.5 65.625C73.5 67.2 72.45 68.25 70.875 68.25H52.5V31.5H73.5V65.625Z"
                            fill="white"
                        />
                    </svg>
                </template>
            </FeatureCard>

            <FeatureCard
                title="Different ways to collect data"
                description="Text fields, check boxes, file upload and
                    other input elements."
            >
                <template #icon>
                    <svg
                        class="flex-shrink-0 w-[74px] lg:w-14"
                        viewBox="0 0 76 76"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <path d="M52.25 2.375H23.75C14.4875 2.375 7.125 9.7375 7.125 19C7.125 28.2625 14.4875 35.625 23.75 35.625H52.25C61.5125 35.625 68.875 28.2625 68.875 19C68.875 9.7375 61.5125 2.375 52.25 2.375ZM52.25 28.5C47.025 28.5 42.75 24.225 42.75 19C42.75 13.775 47.025 9.5 52.25 9.5C57.475 9.5 61.75 13.775 61.75 19C61.75 24.225 57.475 28.5 52.25 28.5Z" fill="white"/>
                        <path d="M52.25 40.375H23.75C14.4875 40.375 7.125 47.7375 7.125 57C7.125 66.2625 14.4875 73.625 23.75 73.625H52.25C61.5125 73.625 68.875 66.2625 68.875 57C68.875 47.7375 61.5125 40.375 52.25 40.375ZM23.75 66.5C18.525 66.5 14.25 62.225 14.25 57C14.25 51.775 18.525 47.5 23.75 47.5C28.975 47.5 33.25 51.775 33.25 57C33.25 62.225 28.975 66.5 23.75 66.5Z" fill="white"/>
                    </svg>
                </template>
            </FeatureCard>

            <FeatureCard
                class="translate-x-8 translate-y-8 xs:transform-none"
                title="Attractive UI"
                description="Make users more interested in your survey with modern
                    UI an UX design."
            >
                <template #icon>
                    <svg
                        class="flex-shrink-0 w-14 lg:w-10"
                        viewBox="0 0 58 76"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <path d="M55 38V59.6666C55 66.8465 43.3594 72.6666 29 72.6666C14.6406 72.6666 3 66.8465 3 59.6666V38M55 38V16.3333M55 38C55 45.1799 43.3594 51 29 51C14.6406 51 3 45.1799 3 38M3 38V16.3333M55 16.3333C55 9.15363 43.3594 3.33331 29 3.33331C14.6406 3.33331 3 9.15363 3 16.3333M55 16.3333C55 23.513 43.3594 29.3333 29 29.3333C14.6406 29.3333 3 23.513 3 16.3333" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </template>
            </FeatureCard>
        </ul>
    </section>
</template>

<style scoped>
.circle-grid-background-decoration {
    @apply absolute w-96 h-96;
    background-image: url('~/assets/images/grid-pattern.png');
    mix-blend-mode: screen;
}

.circle-grid-background-decoration.left {
    @apply -left-32 top-1/2 -translate-y-1/2;
}

.circle-grid-background-decoration.right {
    @apply -right-20 top-10 m:hidden;
}

.circle-grid-background-decoration.bottom {
    @apply left-1/2 -bottom-5 -translate-x-1/2 m:hidden;
}
</style>
