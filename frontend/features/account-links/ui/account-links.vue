<script setup lang="ts">
import { useCurrentAccountStore } from '~/shared/model/current-account-store'

const { account } = storeToRefs(useCurrentAccountStore())
</script>

<template>
    <NuxtLink
        v-if="account"
        to="/dashboard"
        class="flex items-center gap-x-2 ml-auto
            transition-colors duration-300 hover:text-neutral-300"
    >
        <svg class="w-5" viewBox="0 0 21 22" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M17.625 1.5H3.375C2.06332 1.5 1 2.56332 1 3.875V18.125C1 19.4367 2.06332 20.5 3.375 20.5H17.625C18.9367 20.5 20 19.4367 20 18.125V3.875C20 2.56332 18.9367 1.5 17.625 1.5Z" stroke="white" stroke-width="2" stroke-linecap="round"/>
            <path d="M1 7.4375H20" stroke="white" stroke-width="2" stroke-linecap="round"/>
            <path d="M6.9375 8.625V20.5" stroke="white" stroke-width="2" stroke-linecap="round"/>
        </svg>

        Dashboard
    </NuxtLink>

    <div class="flex items-center gap-x-6 ml-auto">
        <AuthDialog />
    </div>
</template>
