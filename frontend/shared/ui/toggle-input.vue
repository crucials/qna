<script setup lang="ts">
defineProps<{
    modelValue: boolean
}>()

const emit = defineEmits<{
    (event: 'update:modelValue', newValue: boolean): void
}>()
</script>

<template>
    <label class="flex items-center gap-x-3 hover:cursor-pointer w-fit">
        <input
            type="checkbox"
            :checked="modelValue"
            class="hidden"
            @change="(event : Event) =>
                emit('update:modelValue', (event.target as HTMLInputElement).checked)"
        >

        <span class="xs:text-sm">
            <slot></slot>
        </span>

        <div
            class="transition-all duration-300 w-16 p-1 rounded-3xl
                shadow-xl shadow-transparent"
            :class="{
                'bg-amethyst shadow-white/20': modelValue,
                'bg-neutral-700': !modelValue
            }"
        >
            <div
                class="h-6 w-6 rounded-full bg-neutral-900 transition-all duration-300"
                :class="{ 'translate-x-8 bg-white': modelValue }"
            ></div>
        </div>
    </label>
</template>
