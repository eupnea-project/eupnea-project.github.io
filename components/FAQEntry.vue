<script setup>
defineProps({
    question: {
        type: String,
        required: true
    }
});
</script>

<template>
    <details class="details custom-block faq-entry" :open="true">
        <summary>
            <h3>{{ question }}</h3>
        </summary>

        <slot></slot>
    </details>
</template>

<style>
.faq-entry summary {
    font-size: 20px;
}

.faq-entry h3 {
    display: inline;
    margin-top: 0;
}
</style>