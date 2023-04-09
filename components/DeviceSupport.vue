<script setup>
import { computed, ref, watch } from "vue";

import DeviceInfo from "./DeviceInfo.vue";
import Dropdown from "./Dropdown.vue";

import jsonAuto from "/device-support/devices-list.json";

const brands = Object.keys(jsonAuto);

const selectedBrand = ref(brands[0]);
const models = computed(() => Object.keys(jsonAuto[selectedBrand.value]));

const selectedModel = ref("");

// Select first available model whenever switching brands
watch(selectedBrand,
    (_) => selectedModel.value = models.value[0],
    { immediate: true }
);

// selected model info
const M = computed(() => jsonAuto[selectedBrand.value][selectedModel.value]);
</script>

<template>
    <Dropdown label="Manufacturer" :options="brands" v-model="selectedBrand" />
    <Dropdown label="Model" :options="models" v-model="selectedModel" class="wide" />

    <DeviceInfo :codename="M.code_name" :boardname="M.family_name" :platform="M.cpu_gen" :depthbootAvailable="M.supported"
        :audioSupport="M.audio_status" :comment="M.comment" />
</template>
