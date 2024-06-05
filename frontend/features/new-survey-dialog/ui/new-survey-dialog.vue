<script setup lang="ts">
import { useNotificationsStore } from '~/shared/model/notifications-store'
import type { Survey } from '~/shared/model/survey'

const props = defineProps<{
    survey: Survey | null
    opened: boolean
}>()

const emit = defineEmits<{
    (event: 'update:opened', newValue: boolean): void
}>()

const { showNotification } = useNotificationsStore()

const newSurveyUrl = computed(() => `${window.origin}/${props.survey?._id}`)

async function copy() {
    try {
        await navigator.clipboard.writeText(newSurveyUrl.value)
        showNotification({
            type: 'success',
            message: 'Link copied'
        })
    }
    catch(error) {
        showNotification({
            type: 'error',
            message: 'Couldn\'t copy the link. Select it and copy it yourself'
        })
    }
}
</script>

<template>
    <DialogWindow
        :opened="opened"
        @update:opened="newValue => emit('update:opened', newValue)"
    >
        <div v-if="survey">
            <img
                src="~/assets/images/checkmark-icon.png"
                alt="Check mark"
                class="w-32 mx-auto mb-6"
            />

            <h2 class="text-2xl font-bold mb-4 text-center">
                Your survey was saved
            </h2>

            <p class="mb-5 text-center">
                Click on the link to copy
            </p>

            <button
                class="p-4 bg-neutral-800 rounded-lg flex items-center gap-x-4 text-neutral-500 w-full group"
                title="Copy"
                @click="copy"
            >
                <svg class="w-5" viewBox="0 0 315 315" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                        fill-rule="evenodd"
                        clip-rule="evenodd"
                        d="M87.3472 35.0139H223.327C242.777 35.0139 249.825 37.0374 256.925 40.8403C264.025 44.6432 269.607 50.2254 273.41 57.3253C277.213 64.4252 279.236 71.4728 279.236 90.9233V226.903C279.236 231.529 281.074 235.966 284.345 239.238C287.617 242.509 292.054 244.347 296.681 244.347C301.307 244.347 305.744 242.509 309.016 239.238C312.287 235.966 314.125 231.529 314.125 226.903V89.5801C314.125 58.4767 310.88 47.1901 304.81 35.8163C298.861 24.5787 289.671 15.3891 278.434 9.44033C267.06 3.36967 255.773 0.125 224.67 0.125H87.3472C82.7207 0.125 78.2836 1.96289 75.0121 5.23436C71.7407 8.50583 69.9028 12.9429 69.9028 17.5694C69.9028 22.196 71.7407 26.6331 75.0121 29.9045C78.2836 33.176 82.7207 35.0139 87.3472 35.0139ZM222.036 75.7292C214.936 71.9263 207.888 69.9028 188.438 69.9028H56.0344C36.5839 69.9028 29.5363 71.9263 22.4364 75.7292C15.413 79.4473 9.6695 85.1908 5.95145 92.2142C2.14856 99.3141 0.125 106.362 0.125 125.812V258.216C0.125 277.649 2.14856 284.714 5.95145 291.814C9.75434 298.913 15.3366 304.496 22.4364 308.299C29.5363 312.101 36.5839 314.125 56.0344 314.125H188.438C207.871 314.125 214.936 312.101 222.036 308.299C229.136 304.496 234.718 298.913 238.521 291.814C242.324 284.714 244.347 277.666 244.347 258.216V125.812C244.347 106.362 242.324 99.3141 238.521 92.2142C234.803 85.1908 229.059 79.4473 222.036 75.7292Z"
                        class="transition-colors duration-300 fill-neutral-600 group-hover:fill-white"
                    />
                </svg>
                {{ newSurveyUrl }}
            </button>
        </div>
    </DialogWindow>
</template>
