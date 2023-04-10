<script setup>
const { comment } = defineProps({
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
    <p>Can boot Depthboot:
        <b :data-color="depthbootAvailable ? 'good' : 'bad'">
            {{ depthbootAvailable ? "Yes" : "No" }}
        </b>
    </p>

    <p>Audio support:
        <b :data-color="audioSupport === 'Full' ? 'good' : 'bad'">
            {{ audioSupport }}
        </b>
    </p>

    <p>Other issues:
        <b v-if="!comment || comment === 'N/A'" data-color="good">N/A</b>
        <b v-else data-color="bad">
            {{ comment ?? "N/A" }}
        </b>
    </p>

    <span id="deviceInfo">
        CPU Generation: <b>{{ platform }}</b><br>
        Codename: <b>{{ codename }} ({{ boardname }})</b>
    </span>
</template>