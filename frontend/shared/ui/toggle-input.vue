<script setup lang="ts">
defineProps<{
    modelValue: boolean
}>()

const emit = defineEmits<{
    (event: 'update:modelValue', newValue: boolean): void
}>()
</script>

<template>
    <div class="flex items-center gap-x-3 hover:cursor-pointer w-fit">
        <span class="xs:text-sm">
            <slot></slot>
        </span>

        <button
            class="transition-all duration-300 w-16 p-1 rounded-3xl
                shadow-xl shadow-transparent"
            :class="{
                'bg-amethyst shadow-white/20': modelValue,
                'bg-neutral-700': !modelValue
            }"
            tabindex="0"
            :aria-pressed="modelValue"
            type="button"
            @click="emit('update:modelValue', !modelValue)"
        >
            <div
                class="h-6 w-6 rounded-full bg-neutral-900 transition-all duration-300"
                :class="{ 'translate-x-8 bg-white': modelValue }"
            ></div>
        </button>
    </div>
</template>
