<script setup lang="ts">
/**
 * visibility can be controlled through v-model or by using
 * the `triggerButton` slot
*/
import { onKeyStroke } from '@vueuse/core'
import { computed, ref } from 'vue'

const props = withDefaults(defineProps<{
    opened?: boolean
    heading?: string
    triggerButtonContainerClass?: string
}>(), { opened: undefined })

const emit = defineEmits<{
    (event: 'update:opened', newValue: boolean): void
}>()

const openedWithTriggerButton = ref(false)

const dialogOpened = computed(() => {
    if(props.opened === undefined) {
        return openedWithTriggerButton.value
    }
    else {
        return props.opened
    }
})

function changeOpenedState(newValue: boolean) {
    if(props.opened === undefined) {
        openedWithTriggerButton.value = newValue
    }
    else {
        emit('update:opened', newValue)
    }
}

onKeyStroke('Escape', () => {
    changeOpenedState(false)
})
</script>

<template>
    <div
        @click="changeOpenedState(true)"
        class="w-fit"
        :class="triggerButtonContainerClass"
    >
        <slot name="triggerButton"></slot>
    </div>

    <Transition enter-from-class="opacity-0">
        <div
            v-show="dialogOpened"
            class="fixed bg-black/40 w-full h-screen top-0 left-0 z-30
                transition-opacity duration-100"
            @mousedown="changeOpenedState(false)"
        ></div>
    </Transition>

    <dialog
        v-bind="$attrs"
        class="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2
            min-w-5 min-h-3 bg-neutral-900 p-6 rounded-lg
            mx-0 block text-white z-30
            origin-center scale-0 open:scale-100 transition-transform duration-300
            sm:min-w-2.5 sm:w-11/12 sm:p-4"
        :open="dialogOpened"
    >
        <h3 v-if="heading" class="text-2xl font-bold tracking-wide mb-6">
            {{ heading }}
        </h3>

        <slot></slot>

        <!-- <button class="absolute top-5 right-4 p-2 rounded-full hover:bg-neutral-800" @click="changeOpenedState(false)">
            <CrossIcon />
        </button> -->
    </dialog>
</template>
