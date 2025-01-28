<script setup lang="ts">
definePageMeta({
    path: '/auth-callback',
})

const route = useRoute()
const googleAuthData = new URLSearchParams(route.hash)
</script>

<template>
    {{ googleAuthData.entries().toArray() }}
</template>

<style scoped></style>
