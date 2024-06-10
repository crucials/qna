<template>
    <div class="flex flex-col min-h-screen overflow-x-hidden">
        <Navigation />
        <main class="flex-grow px-16 py-12 lg:py-9 lg:px-12 sm:p-7 xs:p-5">
            <slot />
        </main>

        <Notifications />
    </div>    
</template>
