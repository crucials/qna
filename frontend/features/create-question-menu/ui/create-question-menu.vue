<script setup lang="ts">
import {
    OPTIONS_QUESTION_TYPES,
    type Question,
    type QuestionType
} from '~/shared/model/question'

const emit = defineEmits<{
    (event: 'create-question', question: Question): void
}>()

function createQuestion(type: QuestionType) {
    emit('create-question', {
        text: '',
        options: OPTIONS_QUESTION_TYPES.includes(type) ? [] : null,
        optional: false,
        type
    })
}
</script>

<template>
    <DropdownMenu
        button-text="Add question"
        class="ml-auto lg:ml-0"
        dropdown-list-class="w-80 lg:right-auto lg:left-0 lg:w-60"
    >
        <DropdownOption @click="createQuestion('SHORT_TEXT')">
            <svg class="w-6" viewBox="0 0 23 9" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g clip-path="url(#clip0_103_66)">
                    <path d="M1.64258 16.8636H13.964M1.64258 11.9545H21.3569M1.64258 7.04544H13.964M1.64258 2.13635H21.3569" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </g>
                <defs>
                    <clipPath id="clip0_103_66">
                        <rect width="23" height="9" fill="white"/>
                    </clipPath>
                </defs>
            </svg>
            Short text
        </DropdownOption>

        <DropdownOption @click="createQuestion('MULTILINE_TEXT')">
            <svg class="w-6" viewBox="0 0 23 19" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M1.64258 16.8636H13.964M1.64258 11.9545H21.3569M1.64258 7.04546H13.964M1.64258 2.13637H21.3569" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            Long text
        </DropdownOption>

        <DropdownOption @click="createQuestion('ONE_OPTION')">
            <svg class="w-6" viewBox="0 0 23 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M11.5 6.25C10.4679 6.25 9.50961 6.50801 8.625 7.02404C7.74038 7.54006 7.04006 8.24038 6.52404 9.125C6.00801 10.0096 5.75 10.9679 5.75 12C5.75 13.0321 6.00801 13.9904 6.52404 14.875C7.04006 15.7596 7.74038 16.4599 8.625 16.976C9.50961 17.492 10.4679 17.75 11.5 17.75C12.5321 17.75 13.4904 17.492 14.375 16.976C15.2596 16.4599 15.9599 15.7596 16.476 14.875C16.992 13.9904 17.25 13.0321 17.25 12C17.25 10.9679 16.992 10.0096 16.476 9.125C15.9599 8.24038 15.2596 7.54006 14.375 7.02404C13.4904 6.50801 12.5321 6.25 11.5 6.25ZM11.5 0.5C9.41747 0.5 7.48237 1.02524 5.69471 2.07572C3.96234 3.08934 2.58934 4.46234 1.57572 6.19471C0.52524 7.98237 0 9.91747 0 12C0 14.0825 0.52524 16.0176 1.57572 17.8053C2.58934 19.5377 3.96234 20.9107 5.69471 21.9243C7.48237 22.9748 9.41747 23.5 11.5 23.5C13.5825 23.5 15.5176 22.9748 17.3053 21.9243C19.0377 20.9107 20.4107 19.5377 21.4243 17.8053C22.4748 16.0176 23 14.0825 23 12C23 9.91747 22.4748 7.98237 21.4243 6.19471C20.4107 4.46234 19.0377 3.08934 17.3053 2.07572C15.5176 1.02524 13.5825 0.5 11.5 0.5ZM11.5 21.2055C9.84135 21.2055 8.29327 20.7817 6.85577 19.9339C5.47356 19.123 4.377 18.0264 3.56611 16.6442C2.71835 15.2067 2.29447 13.6587 2.29447 12C2.29447 10.3413 2.71835 8.79327 3.56611 7.35577C4.377 5.97356 5.47356 4.877 6.85577 4.06611C8.29327 3.21835 9.84135 2.79447 11.5 2.79447C13.1587 2.79447 14.7067 3.21835 16.1442 4.06611C17.5264 4.877 18.623 5.97356 19.4339 7.35577C20.2817 8.79327 20.7055 10.3413 20.7055 12C20.7055 13.6587 20.2817 15.2067 19.4339 16.6442C18.623 18.0264 17.5264 19.123 16.1442 19.9339C14.7067 20.7817 13.1587 21.2055 11.5 21.2055Z" fill="white"/>
            </svg>
            One option
        </DropdownOption>

        <!-- <DropdownOption @click="createQuestion('MULTIPLE_OPTIONS')">
            <svg width="23" height="24" viewBox="0 0 23 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M5.75 6.25V1.65C5.75 1.345 5.87116 1.05249 6.08683 0.836827C6.30249 0.62116 6.595 0.5 6.9 0.5H21.85C22.155 0.5 22.4475 0.62116 22.6632 0.836827C22.8788 1.05249 23 1.345 23 1.65V16.6C23 16.905 22.8788 17.1975 22.6632 17.4132C22.4475 17.6288 22.155 17.75 21.85 17.75H17.25V22.3419C17.25 22.9813 16.7337 23.5 16.092 23.5H1.15805C1.00593 23.5002 0.855274 23.4703 0.714705 23.4122C0.574136 23.354 0.446413 23.2687 0.338848 23.1611C0.231283 23.0536 0.145987 22.9259 0.0878436 22.7853C0.0296997 22.6447 -0.000150716 22.4941 5.72194e-07 22.3419L0.0034506 7.40805C0.0034506 6.76865 0.5198 6.25 1.1615 6.25H5.75ZM8.05 6.25H16.092C16.7313 6.25 17.25 6.76635 17.25 7.40805V15.45H20.7V2.8H8.05V6.25ZM7.47845 18.9L13.9829 12.3945L12.3568 10.7683L7.47845 15.6478L5.037 13.2075L3.4109 14.8336L7.47845 18.9Z" fill="white"/>
            </svg>
            Multiple options
        </DropdownOption> -->
    </DropdownMenu>
</template>
