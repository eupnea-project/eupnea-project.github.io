<script setup>
import VueMultiselect from "vue-multiselect";

defineProps({
    label: {
        type: String
    },
    entryKey: {
        type: String
    },
    entryLabel: {
        type: Function
    },
    placeholder: {
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
    <VueMultiselect :options="options" :value="value" :allowEmpty="false" :label="entryKey" :customLabel="entryLabel"
        :placeholder="placeholder">
        <template v-slot:clear>
            <label>{{ label }}</label>
        </template>
        <template v-slot:noResult>No matching results.</template>
    </VueMultiselect>
</template>
