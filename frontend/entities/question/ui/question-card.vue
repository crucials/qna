<script setup lang="ts">
import type { Question } from '~/entities/question/model/question'

const props = withDefaults(defineProps<{
    question: Question
    orderNumber?: number
    tag?: string
}>(), { tag: 'li' })

const emit = defineEmits<{
    (event: 'update:question', newValue: Question): void
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
            class="text-amethyst mb-0.5"
            v-if="orderNumber"
        >
            Question {{ orderNumber }}
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

        <TextField
            v-if="question.type === 'SHORT_TEXT' || question.type === 'MULTILINE_TEXT'"
            v-model="answer"
            disabled
            :multiline="question.type === 'MULTILINE_TEXT'"
            rows="6"
            placeholder="Answer would be typed here"
            class="mb-7"
        />

        <div
            v-if="question.type === 'ONE_OPTION' && question.options"
            class="mb-7"
        >
            <RadioButtons
                v-model="answer"
                :options="question.options"
                :name="question.text"
                removable-options
                @remove-option="option => emit('update:question', {
                    ...question,
                    options: question.options?.filter(
                        someOption => someOption !== option
                    ) || []
                })"
                disabled
                class="mb-6"
            />

            <div class="flex gap-x-5">
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
