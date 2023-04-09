<script setup>
const { model, name } = defineProps({
    codename: {
        type: String,
    },
    boardname: {
        type: String,
    },
    platform: {
        type: String,
    },
    depthbootAvailable: {
        type: Boolean,
    },
    audioSupport: {
        type: String
    },
    comment: {
        type: String
    }
});
</script>

<template>
    <p>Can boot Depthboot: <b>{{ depthbootAvailable ? "Yes" : "No" }}</b></p>

    <p>Audio support: <b>{{ audioSupport }}</b></p>

    <p>Other issues: <span>{{ comment ?? "N/A" }}</span></p>

    <span id="deviceInfo">
        CPU Generation: <b>{{ platform }}</b><br>
        Codename: <b>{{ codename }} ({{ boardname }})</b>
    </span>
</template>