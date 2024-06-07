<script setup lang="ts">
defineProps<{
    opened: boolean
}>()
const emit = defineEmits<{
    (event: 'update:opened', newValue: boolean): void
}>()
</script>

<template>
    <DialogWindow
        :opened="opened"
        @update:opened="newValue => emit('update:opened', newValue)"
    >
        <img
            src="~/assets/images/checkmark-icon.png"
            alt="Check mark"
            class="w-32 mx-auto mb-6"
        />

        <h2 class="text-2xl font-bold mb-6 text-center">
            Your response was successfully saved
        </h2>

        <NuxtLink to="/">
            <OutlinedButton class="block mx-auto">
                Go to main page
            </OutlinedButton>
        </NuxtLink>
    </DialogWindow>    
</template>
