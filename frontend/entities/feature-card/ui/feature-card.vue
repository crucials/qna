<script setup lang="ts">
defineProps<{
    title: string
    description?: string
}>()
</script>

<template>
    <li
        class="p-7 bg-neutral-600/5 rounded-lg
            backdrop-blur-[2px] border border-neutral-700 flex items-center gap-x-5
            transition-transform duration-300 hover:scale-105"
    >
        <slot name="icon"></slot>

        <div>
            <h3 class="text-xl font-bold mb-3">
                {{ title }}
            </h3>

            <p v-if="description" class="text-neutral-500 font-inria-serif">
                {{ description }}
            </p>
        </div>
    </li>
</template>
