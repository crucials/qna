<script setup lang="ts">
withDefaults(defineProps<{
    pathsClass?: string
}>(), { pathsClass: 'stroke-white' })
</script>

<template>
    <svg class="w-3.5" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M1 1L11 11" stroke-linecap="round" :class="pathsClass" />
        <path d="M1 11L11 1" :class="pathsClass" stroke-linecap="round"/>
    </svg>    
</template>
