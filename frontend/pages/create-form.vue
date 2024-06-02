<script setup lang="ts">
import authorizedOnlyMiddleware from '~/shared/model/authorized-only-middleware'

definePageMeta({
    path: '/surveys/create',
    middleware: authorizedOnlyMiddleware
})
</script>

<template>
    <h1 class="font-bold text-4xl mb-10 sm:text-3xl">
        Create survey
    </h1>
</template>
