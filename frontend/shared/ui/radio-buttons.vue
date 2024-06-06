<script setup lang="ts">
defineProps<{
    modelValue: string | null
    options: string[]
    name: string
    disabled?: boolean
    removableOptions?: boolean
}>()

const emit = defineEmits<{
    (event: 'update:modelValue', newValue: string): void
    (event: 'remove-option', option: string): void
}>()
</script>

<template>
    <div>
        <label
            v-for="option in options"
            :key="option"
            class="mb-5 last-of-type:mb-0 w-fit min-w-48
                flex gap-x-3 items-center"
            :class="{ 'hover:cursor-pointer': !disabled }"
        >
            <input
                type="radio"
                :value="option"
                @change="emit('update:modelValue', option)"
                :name="name"
                hidden
                :disabled="disabled"
            />
            
            <span
                class="inline-block w-5 h-5 rounded-full transition-colors duration-300"
                :class="{
                    'border-neutral-700 border': modelValue !== option,
                    'border-amethyst border-[6px]': modelValue === option,
                    'opacity-70': disabled
                }"
            ></span>

            <span class="inline-block">
                {{ option }}
            </span>

            <button
                v-if="removableOptions"
                type="button"
                class="ml-2 p-2 rounded-full bg-neutral-900
                    hover:scale-110 transition-transform"
                title="Remove option"
                @click="emit('remove-option', option)"
            >
                <CrossIcon class="w-3" paths-class="stroke-neutral-600" />
            </button>
        </label>
    </div>
</template>
