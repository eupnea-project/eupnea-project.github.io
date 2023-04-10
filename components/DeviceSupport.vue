<script setup>
import { computed, ref, watch } from "vue";

import DeviceInfo from "./DeviceInfo.vue";
import Dropdown from "./Dropdown.vue";

import jsonAuto from "/device-support/devices-list.json";

function computeFlatModels() {
    const entries = [];
    const firstModels = [];

    for (let brand in jsonAuto) {
        let isFirst = true;
        for (let model in jsonAuto[brand]) {
            const modelInfo = jsonAuto[brand][model];
            const codename = modelInfo.code_name;

            const entry = {
                brand: brand,
                model: model,
                codename: codename
            };

            entries.push(entry);

            if (isFirst) {
                firstModels.push(entry);
                isFirst = false;
            }
        }
    }

    return {
        devices: entries,
        firstModels: firstModels
    };
}

const { devices, firstModels } = computeFlatModels();

const devicesSortedCodename = computed(() => [...devices]
    .sort((a, b) => a.codename.localeCompare(b.codename))
);

const brandModels = computed(() => devices
    .filter((d) => d.brand === device.value.brand)
    .sort((a, b) => a.model.localeCompare(b.model))
);

const device = ref(devicesSortedCodename.value[0]);
const M = computed(() => jsonAuto[device.value.brand][device.value.model]);


function codenameLabel(v) {
    const entriesWithCodename = devices.filter((d) => d.codename === v.codename);
    const entryCount = entriesWithCodename.length;

    if (entryCount == 1) {
        return v.codename;
    }

    return `${v.codename} (${v.model})`;
}
</script>

<template>
    <Dropdown label="Codename (automatic)" :options="devicesSortedCodename" v-model="device" entryKey="codename"
        :entryLabel="codenameLabel" placeholder="Search by codename" :preserveSearch="true" class="wide" />

    <div class="dropdown-row">
        <Dropdown label="Manufacturer" :options="firstModels" v-model="device" entryKey="brand" />
        <Dropdown label="Model" :options="brandModels" v-model="device" entryKey="model" class="wide" />
    </div>

    <DeviceInfo :codename="M.code_name" :boardname="M.family_name" :platform="M.cpu_gen" :depthbootAvailable="M.supported"
        :audioSupport="M.audio_status" :comment="M.comment" />
</template>
