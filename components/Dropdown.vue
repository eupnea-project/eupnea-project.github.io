<script setup>
import VueMultiselect from "vue-multiselect";

const { label, value, options } = defineProps({
    label: {
        type: String
    },
    value: {
        type: String
    },
    options: {
        type: Array,
        required: true
    }
});

defineEmits(["update:value"]);
</script>

<template>
    <VueMultiselect :options="options" :value="value" :allow-empty="false">
        <template v-slot:clear>
            <label>{{ label }}</label>
        </template>
        <template v-slot:noResult>No matching results.</template>
    </VueMultiselect>
</template>
