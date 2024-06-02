<script setup lang="ts">
withDefaults(defineProps<{
    tag?: string
}>(), { tag: 'button' })
</script>

<template>
    <component
        :is="tag"
        class="p-0.5 bg-enchanted-amethyst rounded-md"
        :type="tag === 'button' ? 'button' : undefined"
    >
        <div
            class="py-2.5 px-8 bg-neutral-900 rounded-md text-base xs:text-sm
                transition-all duration-300 hover:bg-neutral-800
                hover:shadow-xl hover:shadow-purple-400/20"
        >
            <slot></slot>
        </div>
    </component>
</template>
