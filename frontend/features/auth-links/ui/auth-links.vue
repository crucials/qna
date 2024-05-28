<script setup lang="ts">
import { useCurrentAccountStore } from '~/shared/model/current-account'

const { account } = storeToRefs(useCurrentAccountStore())
</script>

<template>
    {{ account }}
</template>
