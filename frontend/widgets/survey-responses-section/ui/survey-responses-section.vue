<script setup lang="ts">
import {
    getSurveyResponses
} from '~/widgets/survey-responses-section/api/get-survey-responses'

const props = defineProps<{
    surveyId: string
}>()

const { data: responses, error } = await getSurveyResponses(props.surveyId)

function formatTime(seconds: number) {
    const minutes = String(Math.floor(seconds / 60)).padStart(2, '0')
    const secondsRemain = String(seconds % 60).padStart(2, '0')

    return `${minutes}:${secondsRemain}`
}
</script>

<template>
    <section v-if="responses">
        <h2 class="text-3xl font-bold mb-10">
            Responses
        </h2>

        <TableBase class="max-w-3xl sm:hidden">
            <template #head>
                <tr>
                    <TableCell header>
                        <UserIcon />
                        Name
                    </TableCell>

                    <TableCell header>
                        <ClockIcon />
                        Time (minutes:seconds)
                    </TableCell>

                    <TableCell></TableCell>
                </tr>
            </template>

            <template #body>
                <tr
                    v-for="response, index in responses.data"
                    class="transition-colors hover:bg-neutral-900"
                >
                    <TableCell>
                        {{ response.name || `User ${index}` }}
                    </TableCell>

                    <TableCell>
                        {{ formatTime(response.seconds_spent) }}
                    </TableCell>

                    <TableCell>
                        <NuxtLink
                            :to="`/dashboard/surveys/${surveyId}/responses`"
                            class="hover:underline hover:text-amethyst"
                        >
                            See answers
                        </NuxtLink>
                    </TableCell>
                </tr>
            </template>
        </TableBase>

        <ul class="hidden sm:block">
            <li
                class="bg-neutral-900 rounded-xl p-4
                    flex items-center gap-x-8 flex-wrap gap-y-4
                    mb-6 last:mb-0"
                v-for="response, index in responses.data"
            >
                <div class="flex items-center gap-x-2">
                    <UserIcon />
                    {{ response.name || `User ${index}` }}
                </div>

                <div class="flex items-center gap-x-2">
                    <ClockIcon />
                    {{ formatTime(response.seconds_spent) }}
                </div>

                <NuxtLink
                    :to="`/dashboard/surveys/${surveyId}/responses`"
                    class="hover:underline hover:text-amethyst ml-auto"
                >
                    See answers
                </NuxtLink>
            </li>
        </ul>
    </section>    
</template>
