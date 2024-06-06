<script setup lang="ts">
import type { SurveyWithQuestions } from '~/pages/survey/api/survey-with-questions'
import { useAnswersStore } from '~/shared/model/answers-store'
import type { ApiError } from '~/shared/model/api-response'
import { useForm } from '~/shared/model/form'
import type {
    SurveyResponseFormData
} from '~/widgets/survey-response-form/model/form-data'

const props = defineProps<{
    survey: SurveyWithQuestions
}>()

const emit = defineEmits<{
    (
        event: 'submit-response',
        response: SurveyResponseFormData,
        setError: (error: ApiError) => void
    ): void
}>()

const mounted = useMounted()

const { answers } = storeToRefs(useAnswersStore())
answers.value = props.survey.questions.map(question => ({
    questionId: question._id || '',
    answer: null
}))

const { form, setError } = useForm<SurveyResponseFormData>({
    name: null,
    answers: [],
})

function submitResponse() {
    form.value.data.answers = answers.value
    emit('submit-response', form.value.data, setError)
}
</script>

<template>
    <form>
        <TextField
            v-model="form.data.name"
            placeholder="Your name"
            underlined
            class="max-w-xl mb-16"
        />

        <div class="relative bg-neutral-950 rounded-lg p-7 max-w-6xl min-h-4">
            <!-- question marks background pattern -->
            <svg
                class="absolute right-[3%] top-1/4 scale-0
                    transition-transform duration-500"
                :class="{ 'scale-100': mounted }"
                width="283"
                height="280"
                viewBox="0 0 283 280"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
            >
                <path d="M251.377 133.021C251.962 135.803 250.686 137.524 247.548 138.185L226.802 142.555C225.407 142.849 224.358 142.767 223.655 142.31C223.068 141.829 222.64 140.95 222.372 139.675L217.831 118.119C217.392 116.033 218.102 114.794 219.961 114.402L243.846 109.371C245.473 109.028 246.482 109.784 246.873 111.639L251.377 133.021ZM175.999 48.3163C175.02 48.2803 174.387 47.869 174.1 47.0822C173.813 46.2954 173.712 45.5298 173.798 44.7855C175.736 35.5417 180.064 27.8519 186.783 21.7162C193.477 15.4646 202.113 11.2248 212.689 8.99702C221.406 7.16089 229.196 6.97257 236.058 8.43206C243.012 9.75117 248.721 12.3614 253.184 16.2628C257.739 20.0238 260.615 24.7437 261.811 30.4226C262.958 35.8697 262.772 40.7504 261.253 45.0646C259.734 49.3788 257.607 53.3975 254.871 57.1207C252.135 60.844 249.341 64.5795 246.489 68.3272C243.729 71.9346 241.565 75.7795 239.997 79.8619C238.429 83.9443 238.195 88.5931 239.293 93.8084C239.489 94.7356 239.311 95.6203 238.76 96.4626C238.301 97.1645 237.548 97.6256 236.502 97.8459L222.206 100.857C219.766 101.371 218.264 100.296 217.703 97.6299C216.409 91.4875 216.286 86.0061 217.335 81.1859C218.383 76.3657 220.018 72.027 222.24 68.1699C224.438 64.1969 226.638 60.5258 228.842 57.1568C231.162 53.7632 233.017 50.4676 234.407 47.2699C235.913 44.0477 236.312 40.7562 235.604 37.3952C234.725 33.223 232.46 30.2504 228.81 28.4776C225.159 26.7048 221.009 26.3081 216.36 27.2873C213.338 27.9238 210.496 29.1276 207.835 30.8986C205.173 32.6696 202.97 34.8887 201.226 37.5559C199.481 40.223 198.275 43.14 197.607 46.3067C197.337 47.3317 196.994 48.0091 196.578 48.3389C196.137 48.5527 195.382 48.7118 194.312 48.8163L175.999 48.3163Z" fill="white" fill-opacity="0.03"/>
                <path d="M56.7417 266.54C55.9244 269.263 53.9799 270.163 50.9084 269.241L30.6021 263.144C29.2369 262.734 28.3551 262.16 27.9566 261.422C27.6718 260.719 27.7167 259.743 28.0914 258.495L34.4259 237.396C35.0389 235.354 36.2555 234.606 38.0756 235.153L61.4535 242.171C63.0462 242.649 63.5701 243.796 63.0252 245.611L56.7417 266.54ZM31.1199 156.085C30.278 155.585 29.9193 154.921 30.0439 154.093C30.1686 153.264 30.4468 152.544 30.8787 151.932C37.0051 144.744 44.4866 140.065 53.323 137.895C62.1935 135.612 71.8049 136.024 82.1571 139.132C90.6892 141.694 97.6181 145.258 102.944 149.825C108.417 154.312 112.179 159.337 114.23 164.899C116.428 170.382 116.693 175.902 115.024 181.461C113.424 186.792 110.924 190.988 107.525 194.049C104.126 197.109 100.334 199.619 96.1494 201.577C91.9649 203.536 87.7235 205.478 83.4252 207.403C79.2747 209.248 75.534 211.588 72.203 214.421C68.872 217.255 66.4403 221.224 64.9077 226.329C64.6353 227.236 64.0556 227.928 63.1687 228.403C62.4296 228.8 61.5482 228.844 60.5243 228.537L46.5317 224.336C44.1427 223.619 43.3399 221.956 44.1232 219.347C45.9282 213.334 48.4447 208.463 51.6728 204.733C54.9009 201.003 58.4137 197.977 62.2113 195.655C66.043 193.219 69.7326 191.05 73.2802 189.147C76.9416 187.278 80.148 185.273 82.8992 183.131C85.7643 181.023 87.6906 178.325 88.6783 175.035C89.9043 170.951 89.3391 167.257 86.9828 163.953C84.6264 160.649 81.173 158.313 76.6226 156.947C73.6648 156.059 70.5936 155.755 67.409 156.036C64.2244 156.317 61.2279 157.21 58.4193 158.716C55.6108 160.223 53.1552 162.206 51.0524 164.666C50.3249 165.437 49.6996 165.868 49.1764 165.958C48.6873 165.935 47.9478 165.713 46.9581 165.292L31.1199 156.085Z" fill="white" fill-opacity="0.03"/>
            </svg>

            <div class="relative">
                <QuestionCard
                    v-for="question, index in survey.questions"
                    :question="question"
                    :order-number="index + 1"
                    class="mb-6"
                />

                <SolidButton
                    class="relative overflow-hidden group"
                    @click="submitResponse"
                >
                    <div
                        class="bg-enchanted-amethyst absolute top-0 left-0 h-full w-full
                            transition-opacity duration-300 group-hover:opacity-0"
                    ></div>
                    <span class="relative">Send</span>
                </SolidButton>
            </div>
        </div>
    </form>    
</template>
