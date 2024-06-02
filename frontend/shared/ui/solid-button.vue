<script setup lang="ts">
withDefaults(defineProps<{
    tag?: string
}>(), { tag: 'button' })
</script>

<template>
    <component
        :is=tag
        class="block py-2.5 px-8 bg-amethyst rounded-md text-base xs:text-sm
            transition-colors duration-300 hover:bg-amethyst-dark"
    >
        <slot></slot>
    </component>
</template>
