<script setup lang="ts">

</script>

<template>
    <DialogWindow class="p-3.5 w-2/5">
        <template #triggerButton>
            <button
                class="font-medium text-lg lg:text-base transition-colors
                    hover:text-neutral-300"
            >
                Log in
            </button>
        </template>

        <div class="flex items-start gap-x-6">
            <img
                src="~/assets/images/abstract-illustration.jpg"
                alt="Abstract wavy illustration"
                class="w-[290px] rounded-2xl"
            />

            <form @submit.prevent="" class="p-4">
                <h2 class="text-2xl font-bold mb-6">
                    welcome to qna
                </h2>

                
            </form>
        </div>
    </DialogWindow>
</template>
