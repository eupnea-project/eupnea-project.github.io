<script setup>
defineProps({
    question: {
        type: String,
        required: true
    }
});
</script>

<template>
    <details class="faq-entry">
        <summary>
            {{ question }}
            <!-- <h3>{{ question }}</h3> -->
        </summary>

        <div class="faq-answer">
            <slot></slot>
        </div>
    </details>
</template>

<style>
.faq-entry {
    margin: 16px 0;
    color: var(--vp-custom-block-details-text);
    background-color: var(--vp-custom-block-details-bg);
    transition: 0.3s;

    border: 1px solid var(--vp-custom-block-details-border);
    border-radius: 8px;
}

.faq-entry summary {
    font-size: 20px;
    cursor: pointer;
    margin: 0;
    transition: 0.1s;
    padding: 16px 20px;
}
.faq-entry summary:hover {
    color: var(--vp-c-text-1);
}

.faq-answer {
    padding: 0 20px;
}

.faq-answer > :first-child {
    margin-top: 0;
}

.faq-entry[open] {
    color: var(--vp-c-text-1);
    border-color: var(--vp-custom-block-tip-border);
}
.faq-entry[open] summary {
    color: var(--vp-c-text-1);
    border-color: var(--vp-custom-block-tip-border);
}
</style>