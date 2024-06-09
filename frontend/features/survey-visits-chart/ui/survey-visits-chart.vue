<script setup lang="ts">
import { Chart, LinearScale, BarController, CategoryScale, BarElement } from 'chart.js'
import type { SurveyStats } from '~/entities/survey-stats/model/survey-stats'

const props = defineProps<{
    stats: SurveyStats
}>()

onMounted(() => {
    const chartCanvasElement = document.getElementById('surveyVisitsChart')

    const formattedDates = props.stats.weekly_page_visits.map(record => {
        return new Date(record.date).toLocaleDateString(undefined, {
            weekday: 'long'
        })
    })

    Chart.register(LinearScale, BarController, CategoryScale, BarElement)
    Chart.defaults.font.family = 'Libre Franklin'
    Chart.defaults.font.weight = 400
    Chart.defaults.font.size = 16
    Chart.defaults.color = 'white'

    const chart = new Chart(chartCanvasElement as HTMLCanvasElement, {
        type: 'bar',
        data: {
            labels: formattedDates,
            datasets: [{
                label: 'Page visits count',
                data: props.stats.weekly_page_visits.map(record => record.count),
                backgroundColor: '#A965D7',
                barThickness: 40,
                borderRadius: 10
            }],
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        tickWidth :0,
                        display: true,
                        color: '#FFFFFF10'
                    }
                }
            }
        }
    })
    console.log(chart.data)
})
</script>

<template>
    <canvas id="surveyVisitsChart"></canvas>    
</template>
