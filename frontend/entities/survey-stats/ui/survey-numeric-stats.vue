<script setup lang="ts">
import type { SurveyStats } from '~/entities/survey-stats/model/survey-stats'
import { useAppearAnimation } from '~/shared/utils/appear-animation'

const props = defineProps<{
    stats: SurveyStats
}>()

const { readyToAnimate } = useAppearAnimation()

const sentResponsesPercentage = computed(() => {
    if(props.stats.total_visits_count === 0) {
        return 0
    }
    
    return Math.min(
        props.stats.responses_count / props.stats.total_visits_count * 100, 100
    )
})
</script>

<template>
    <div
        class="p-px rounded-xl bg-silver lg:col-span-2 sm:col-span-full
            transition-transform duration-300 scale-0"
        :class="{ 'scale-100': readyToAnimate }"
    >
        <article class="bg-neutral-950 rounded-xl p-6 h-full">
            <header class="flex items-center gap-x-4 mb-6">
                <BarChartIcon />

                <b class="font-semibold text-3xl lg:text-2xl">
                    {{ stats.total_visits_count }}
                </b>
            </header>

            <p class="text-lg lg:text-base">
                times someone visited this survey
            </p>
        </article>
    </div>

    <div
        class="p-px rounded-xl bg-silver lg:col-span-2 sm:col-span-full
            transition-transform duration-300 scale-0 delay-100"
        :class="{ 'scale-100': readyToAnimate }"
    >
        <article class="bg-neutral-950 rounded-xl p-6 h-full">
            <header class="flex items-center gap-x-4 mb-6">
                <BarChartIcon />

                <b class="font-semibold text-3xl lg:text-2xl">
                    {{ stats.responses_count }}
                    <sup
                        class="text-lg lg:text-base font-normal"
                        :class="{
                            'text-error':
                                sentResponsesPercentage <= 50,
                            'text-green-500':
                                sentResponsesPercentage > 50
                        }"
                    >
                        ({{ Math.round(sentResponsesPercentage) }}%)
                    </sup>
                </b>
            </header>

            <p class="text-lg lg:text-base">
                times someone submit a response
            </p>
        </article>
    </div>

    <slot name="chart"></slot>

    <div
        class="p-px rounded-xl bg-silver sm:col-span-full
            transition-transform duration-300 scale-0 delay-200 col-span-2"
        :class="{ 'scale-100': readyToAnimate }"
    >
        <article class="bg-neutral-950 rounded-xl p-6 h-full">
            <header class="flex items-center gap-x-4 mb-6">
                <BarChartIcon />

                <b
                    class="font-semibold text-3xl lg:text-2xl"
                    :class="{
                        'text-error':
                            stats.responses_with_optional_question_percentage <= 50,
                        'text-green-500':
                            stats.responses_with_optional_question_percentage > 50
                    }"
                >
                    {{ Math.round(stats.responses_with_optional_question_percentage) }}%
                </b>
            </header>

            <p class="text-lg lg:text-base">
                of users answered at least on one optional question
            </p>
        </article>
    </div>
</template>
