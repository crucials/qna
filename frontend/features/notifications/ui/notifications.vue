<script setup lang="ts">
import { useNotificationsStore } from '@/shared/model/notifications-store'

const { notifications } = storeToRefs(useNotificationsStore())
</script>

<template>
    <TransitionGroup
        tag="ul"
        class="fixed bottom-7 right-7 flex flex-col gap-y-4 w-[410px]
            sm:w-11/12 sm:right-auto sm:left-1/2 sm:-translate-x-1/2"
        enter-from-class="translate-x-12 opacity-0"
        leave-to-class="translate-x-12 opacity-0"
    >
        <li
            v-for="notification in notifications"
            :key="notification.id"
            class="relative transition-all duration-300 overflow-hidden
                bg-neutral-900 rounded-lg px-8 py-6 flex items-center gap-x-6
                xs:px-6 xs:py-5
                before:w-24 before:h-24 before:rounded-full before:absolute
                before:-top-6 before:-left-6 before:blur-2xl"
            :class="{
                'before:bg-amethyst/50': notification.type === 'success',
                'before:bg-error/30': notification.type === 'error'
            }"
        >
            <SuccessNotificationIcon v-if="notification.type === 'success'" />
            <ErrorNotificationIcon v-if="notification.type === 'error'" />

            {{ notification.message }}

            <button
                class="transition-colors duration-300 absolute top-2 rounded-full right-2 p-2
                    hover:bg-neutral-800"
                @click="notifications = notifications.filter(someNotification =>
                    someNotification.id !== notification.id)"
            >
                <CrossIcon />
            </button>
        </li>
    </TransitionGroup>
</template>
