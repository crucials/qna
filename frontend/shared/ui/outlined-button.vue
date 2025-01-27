<script setup lang="ts">
withDefaults(
    defineProps<{
        tag?: string
        color: 'purple' | 'grey'
        buttonClass?: string
    }>(),
    { tag: 'button', color: 'purple', buttonClass: '' },
)

const borderContainerColorStyleClasses = {
    purple: 'p-0.5 bg-enchanted-amethyst',
    grey: 'p-px bg-neutral-700',
}

const buttonColorStylesClasses = {
    purple: 'bg-neutral-900 hover:bg-neutral-800 hover:shadow-xl hover:shadow-purple-400/20',
    grey: 'bg-neutral-800 hover:bg-neutral-700',
}
</script>

<template>
    <component
        :is="tag"
        :class="`rounded-md ${borderContainerColorStyleClasses[color]}`"
        :type="tag === 'button' ? 'button' : undefined"
    >
        <div
            :class="`flex items-center gap-x-3 py-2.5 px-7 rounded-md text-base xs:text-sm transition-all duration-300 ${buttonColorStylesClasses[color]} ${buttonClass}`"
        >
            <slot></slot>
        </div>
    </component>
</template>
