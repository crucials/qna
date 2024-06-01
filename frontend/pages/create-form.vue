<script setup lang="ts">
import authorizedOnlyMiddleware from '~/shared/model/authorized-only-middleware'

definePageMeta({
    path: '/forms/create',
    middleware: authorizedOnlyMiddleware
})
</script>

<template>
    
</template>
