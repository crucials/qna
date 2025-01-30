<script setup lang="ts">
import { getSurveyStats } from '~/pages/dashboard/survey-stats/api/get-survey-stats'
import authorizedOnlyMiddleware from '~/shared/model/authorized-only-middleware'

definePageMeta({
    path: '/dashboard/surveys/:id',
    middleware: authorizedOnlyMiddleware,
})

const router = useRouter()
const id = useRoute().params.id.toString()

const { data: stats, error } = await getSurveyStats(id)

if (error.value?.statusCode === 404) {
    throw createError({
        statusCode: 404,
        message: 'Requested survey not found',
    })
} else if (error.value?.statusCode === 403) {
    router.push('/')
}
</script>

<template>
    <div v-if="stats?.data">
        <section class="mb-24">
            <h1 class="font-normal text-4xl lg:text-3xl mb-12">
                {{ stats.data.survey_title }}
            </h1>

            <div
                class="grid grid-cols-4 grid-rows-[repeat(auto-fit,184px)] gap-7"
            >
                <SurveyNumericStats :stats="stats.data">
                    <template #chart>
                        <div
                            class="p-px rounded-xl bg-silver col-span-2 row-span-2 lg:row-start-2 lg:col-span-full"
                        >
                            <article
                                class="bg-neutral-950 rounded-xl p-6 h-full flex items-center sm:overflow-x-scroll"
                            >
                                <div class="min-w-4 min-h-3.5 h-full w-full">
                                    <SurveyVisitsChart :stats="stats.data" />
                                </div>
                            </article>
                        </div>
                    </template>
                </SurveyNumericStats>
            </div>
        </section>

        <ClientOnly>
            <LazySurveyResponsesSection :survey-id="id" />
        </ClientOnly>
    </div>
</template>
