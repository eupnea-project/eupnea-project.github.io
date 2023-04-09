<script setup>
import VueMultiselect from "vue-multiselect";

const { value, options } = defineProps({
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
        <template v-slot:noResult>No matching results.</template>
    </VueMultiselect>
</template>
