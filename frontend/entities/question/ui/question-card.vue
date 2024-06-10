<script setup lang="ts">
import { OPTIONS_QUESTION_TYPES, type Question } from '~/shared/model/question'

const props = withDefaults(defineProps<{
    question: Question
    orderNumber: number
    tag?: string
    surveyCreationMode?: boolean
}>(), { tag: 'fieldset' })

const emit = defineEmits<{
    (event: 'update:question', newValue: Question): void,
    (event: 'remove-question'): void
}>()

const newOption = ref('')

function addOption() {
    if(props.question.options) {
        emit('update:question', {
            ...props.question,
            options: [...props.question.options, newOption.value]
        })

        newOption.value = ''
    }
}
</script>

<template>
    <component :is="tag" class="max-w-3xl">
        <div
            class="text-amethyst mb-2 flex items-center gap-x-4"
        >
            <button
                v-if="surveyCreationMode"
                type="button"
                class="ml-2 p-1.5 rounded-full bg-neutral-900
                    hover:scale-110 transition-transform"
                title="Remove question"
                @click="emit('remove-question')"
            >
                <CrossIcon class="w-3" paths-class="stroke-neutral-600" />
            </button>
            Question {{ orderNumber }}
        </div>

        <TextField
            v-if="surveyCreationMode"
            :model-value="question.text"
            @update:model-value="newValue => emit('update:question', {
                ...question,
                text: newValue
            })"
            underlined
            placeholder="Enter the question text"
            class="mb-6 text-lg sm:text-base"
        />

        <h3
            v-else
            class="text-xl sm:text-lg"
            :class="{
                'mb-5': !question.optional,
                'mb-1': question.optional
            }"
        >
            {{ question.text }}
        </h3>

        <div
            v-if="!surveyCreationMode && question.optional" 
            class="text-base m:text-sm text-neutral-500 mb-5"
        >
            This question is optional
        </div>

        <QuestionAnswerInput
            :question="question"
            :survey-creation-mode="surveyCreationMode"
            @remove-option="option => emit('update:question', {
                ...question,
                options: question.options?.filter(
                    someOption => someOption !== option
                ) || []
            })"
        />

        <div
            v-if="surveyCreationMode
                && OPTIONS_QUESTION_TYPES.includes(question.type)
                && question.options"
            class="flex gap-x-5 mb-6"
        >
            <TextField
                v-model="newOption"
                placeholder="Option name"
                class="flex-grow"
            />

            <SolidButton
                :disabled="question.options.includes(newOption)
                    || newOption.trim().length === 0"
                @click="addOption"
            >
                Add option
            </SolidButton>
        </div>

        <ToggleInput
            v-if="surveyCreationMode"
            :model-value="question.optional"
            @update:model-value="newValue => emit('update:question', {
                ...question,
                optional: newValue
            })"
        >
            Optional
        </ToggleInput>
    </component>
</template>
