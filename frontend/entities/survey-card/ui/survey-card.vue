<script setup lang="ts">
import type { Survey } from '~/shared/model/survey'

defineProps<{
    survey: Survey
}>()

const emit = defineEmits<{
    (event: 'delete'): void
}>()
</script>

<template>
    <li class="bg-neutral-900 rounded-xl p-6 min-w-3 xs:min-w-2.5 flex flex-col">
        <SurveyIcon class="mb-5" />
        
        <div class="flex gap-x-3.5 items-center mb-6">
            <h3 class="font-semibold text-xl m:text-lg">
                {{ survey.title }}
            </h3>

            <button
                class="p-1.5 rounded-lg transition-colors hover:bg-amethyst/20"
                @click="emit('delete')"
            >
                <svg class="w-5" viewBox="0 0 30 33" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M11.25 16.375V24.9167" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M18.082 16.375V24.9167" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M1 7.83334H28.3333" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M4.41602 12.9583V26.625C4.41602 29.4555 6.71056 31.75 9.54102 31.75H19.791C22.6216 31.75 24.916 29.4555 24.916 26.625V12.9583" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M9.54102 4.41667C9.54102 2.52969 11.0707 1 12.9577 1H16.3743C18.2614 1 19.791 2.52969 19.791 4.41667V7.83333H9.54102V4.41667Z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
            </button>
        </div>  

        <div class="flex gap-4 flex-wrap items-stretch mt-auto">
            <NuxtLink :to="`/dashboard/surveys/${survey._id}`">
                <OutlinedButton class="h-full">
                    Analyze
                </OutlinedButton>
            </NuxtLink>

            <NuxtLink :to="`/${survey._id}`">
                <SolidButton class="h-full">
                    Open
                </SolidButton>
            </NuxtLink>
        </div>
    </li>
</template>
