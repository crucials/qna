<script setup lang="ts">
import { useAnswersStore } from '~/shared/model/answers-store'
import {
    getSurveyResponses,
    type SurveyResponse
} from '~/widgets/survey-responses-section/api/get-survey-responses'

const props = defineProps<{
    surveyId: string
}>()

const { data: responses } = await getSurveyResponses(props.surveyId)

const { answers } = storeToRefs(useAnswersStore())

const answersDialogData = ref({
    senderName: '',
    opened: false
})

function formatTime(seconds: number) {
    const minutes = String(Math.floor(seconds / 60)).padStart(2, '0')
    const secondsRemain = String(seconds % 60).padStart(2, '0')

    return `${minutes}:${secondsRemain}`
}

function seeAnswers(response: SurveyResponse) {
    answers.value = response.answers
    answersDialogData.value = {
        senderName: response.name || '',
        opened: true
    }
}
</script>

<template>
    <section v-if="responses?.data">
        <h2 class="text-3xl font-bold mb-10">
            Responses
        </h2>

        <div v-if="responses.data.length > 0">
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
                            <button
                                class="hover:underline hover:text-amethyst ml-auto"
                                @click="seeAnswers(response)"
                            >
                                See answers
                            </button>
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

                    <button
                        class="hover:underline hover:text-amethyst ml-auto"
                        @click="seeAnswers(response)"
                    >
                        See answers
                    </button>
                </li>
            </ul>
        </div>

        <p v-else class="text-neutral-500 text-lg m:text-base">
            No responses have been sent for now
        </p>

        <AnswersDialog
            v-model:opened="answersDialogData.opened"
            :answers="answers"
            :sender-name="answersDialogData.senderName"
        />
    </section>    
</template>
