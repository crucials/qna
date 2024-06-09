<script setup lang="ts">

</script>

<template>
    <div class="p-px bg-silver rounded-lg">
        <table class="rounded-lg bg-neutral-950 w-full h-full">
            <thead class="border-b border-b-neutral-600">
                <slot name="head"></slot>
            </thead>

            <tbody>
                <slot name="body"></slot>
            </tbody>
        </table>
    </div>
</template>
