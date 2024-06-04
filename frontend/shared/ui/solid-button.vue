<script setup lang="ts">
withDefaults(defineProps<{
    tag?: string
}>(), { tag: 'button' })
</script>

<template>
    <component
        :is=tag
        class="flex items-center gap-x-3
            py-2.5 px-8 bg-amethyst rounded-md text-base xs:text-sm
            transition-colors duration-300 hover:bg-amethyst-dark
            disabled:opacity-70 disabled:hover:bg-amethyst"
        :type="tag === 'button' ? 'button' : undefined"
    >
        <slot></slot>
    </component>
</template>
