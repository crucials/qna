<script setup lang="ts">
defineProps<{
    buttonText: string
    dropdownListClass?: string
}>()

const opened = ref(false)

const dropdownWrapper = ref()

onClickOutside(dropdownWrapper, () => opened.value = false)
</script>

<template>
    <div class="relative" ref="dropdownWrapper">
        <Transition
            enter-from-class="-translate-y-3 opacity-0"
            leave-to-class="-translate-y-3 opacity-0"
        >
            <ul
                v-show="opened"
                role="listbox"
                id="dropdownList"
                class="transition-all duration-300
                    absolute top-[calc(100%+10px)] right-0 z-20
                    flex flex-col gap-y-3
                    p-4 rounded-md bg-black/80 border border-neutral-600"
                :class="dropdownListClass"
                @click="opened = false"
            >
                <slot></slot>
            </ul>
        </Transition>

        <OutlinedButton
            :aria-expanded="opened"
            aria-controls="dropdownList"
            aria-haspopup="listbox"
            class="relative"
            @click="opened = !opened"
        >
            <svg class="w-4" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M10.4528 5H3.94703C3.15848 5 2.71643 5.7917 3.20363 6.3314L6.45653 9.935C6.83453 10.354 7.56428 10.354 7.94333 9.935L11.1962 6.33035C11.6834 5.7917 11.2414 5 10.4528 5Z" fill="white"/>
            </svg>
            {{ buttonText }}
        </OutlinedButton>
    </div>
</template>
