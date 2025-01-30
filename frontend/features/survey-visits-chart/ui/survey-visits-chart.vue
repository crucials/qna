<script setup lang="ts">
import {
    Chart,
    LinearScale,
    BarController,
    CategoryScale,
    BarElement,
    Legend,
} from 'chart.js'
import type { SurveyStats } from '~/entities/survey-stats/model/survey-stats'

const props = defineProps<{
    stats: SurveyStats
}>()

let chart: Chart<'bar'> | undefined = undefined

onMounted(() => {
    const chartCanvasElement = document.getElementById('surveyVisitsChart')

    const formattedDates = props.stats.weekly_page_visits.map((record) => {
        return new Date(record.date).toLocaleDateString(undefined, {
            weekday: 'short',
        })
    })

    if (Legend.defaults) {
        Legend.defaults.onClick = () => {}
    } else {
        Legend.defaults = {
            onClick: () => {},
        }
    }

    Chart.register(
        LinearScale,
        BarController,
        CategoryScale,
        BarElement,
        Legend,
    )

    updateChartOptions()

    chart = new Chart(chartCanvasElement as HTMLCanvasElement, {
        type: 'bar',
        data: {
            labels: formattedDates,
            datasets: [
                {
                    label: 'Page visits count',
                    data: props.stats.weekly_page_visits.map(
                        (record) => record.count,
                    ),
                    backgroundColor: '#A965D7',
                    hoverBackgroundColor: '#ba85e1',
                    barThickness: 40,
                    borderRadius: 10,
                },
            ],
        },
        options: {
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        tickWidth: 0,
                        display: true,
                        color: '#FFFFFF10',
                    },
                },
            },
        },
    })

    window.addEventListener('resize', () => {
        updateChartOptions()
        chart?.update()
    })
})

function updateChartOptions() {
    let barThickness = 40
    if (window.innerWidth <= 600) {
        barThickness = 25
    }

    let fontSize = 16
    if (window.innerWidth <= 1200) {
        fontSize = 14
    }

    Chart.defaults.font.family = 'Libre Franklin'
    Chart.defaults.font.weight = 400
    Chart.defaults.font.size = fontSize
    Chart.defaults.color = 'white'

    if (chart) {
        chart.data.datasets[0].barThickness = barThickness
    }
}
</script>

<template>
    <canvas id="surveyVisitsChart"></canvas>
</template>
