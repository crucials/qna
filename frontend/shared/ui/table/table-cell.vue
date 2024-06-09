<script setup lang="ts">
defineProps<{
    header?: boolean
}>()
</script>

<template>
    <component
        :is="header ? 'th' : 'td'"
        class="text-start font-normal text-lg py-4 px-7
            lg:text-base sm:text-sm m:p-4"
        :class="{ 'text-neutral-500': header }"
    >
        <div class="flex items-center gap-x-3">
            <slot></slot>
        </div>
    </component>
</template>
