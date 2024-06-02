<script setup lang="ts">
import { useForm } from '~/shared/model/form'

const { form, setError } = useForm({
    title: '',
    anonymous: false
})
</script>

<template>
    <form>
        <div class="flex items-center gap-x-12 gap-y-6 lg:flex-wrap">
            <TextField
                v-model="form.data.title"
                placeholder="Enter the survey title"
                underlined
                class="text-2xl lg:text-xl sm:text-lg"
                wrapper-class="w-1/2 min-w-4 sm:w-full sm:min-w-2.5"
            />

            <ToggleInput v-model="form.data.anonymous">
               Anonymous 
            </ToggleInput>
            
            <CreateQuestionMenu />
        </div>
    </form>
</template>
