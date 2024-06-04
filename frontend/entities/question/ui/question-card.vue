<script setup lang="ts">
import { OPTIONS_QUESTION_TYPES, type Question } from '~/entities/question/model/question'

const props = withDefaults(defineProps<{
    question: Question
    orderNumber: number
    tag?: string
}>(), { tag: 'li' })

const emit = defineEmits<{
    (event: 'update:question', newValue: Question): void,
    (event: 'remove-question'): void
}>()

const answer = ref('')
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
            class="text-amethyst mb-0.5 flex items-center gap-x-4"
        >
            Question {{ orderNumber }}
            <button
                type="button"
                class="ml-2 p-2 rounded-full bg-neutral-900
                    hover:scale-110 transition-transform"
                @click="emit('remove-question')"
            >
                <CrossIcon class="w-3" paths-class="stroke-neutral-600" />
            </button>
        </div>

        <TextField
            :model-value="question.text"
            @update:model-value="newValue => emit('update:question', {
                ...question,
                text: newValue
            })"
            underlined
            placeholder="Enter the question title"
            class="mb-6 text-lg sm:text-base"
        />

        <QuestionAnswerInput
            :question="question"
            removable-options
            @remove-option="option => emit('update:question', {
                ...question,
                options: question.options?.filter(
                    someOption => someOption !== option
                ) || []
            })"
            disabled
        />

        <div
            class="flex gap-x-5 mb-6"
            v-if="OPTIONS_QUESTION_TYPES.includes(question.type)
                && question.options"
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
