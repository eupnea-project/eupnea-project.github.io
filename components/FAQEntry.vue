<script setup>
import slugify from "@sindresorhus/slugify";
import { ref } from "vue";

const { question, link } = defineProps({
    question: {
        type: String,
        required: true
    },
    link: {
        type: String
    }
});

const myHash = link ?? slugify(question);

const isOpen = ref(false);

function checkIsActive() {
    const hash = window.location.hash;
    const isActive = hash.substring(1) === myHash;

    if (isActive) {
        isOpen.value = true;
    }
}

function onClick(ev) {
    ev.preventDefault();
    isOpen.value = !isOpen.value;

    if (isOpen.value) {
        const href = new URL(window.location.href);
        href.hash = myHash;
        window.history.replaceState({}, "", href);
    }
}

// window.addEventListener("hashchange", (ev) => {
//     console.log("hash change")
//     // checkIsActive();
//     // ev.preventDefault();
// });

checkIsActive();
</script>

<template>
    <details class="faq-entry" :open="isOpen" :id="myHash">
        <summary>
            <a class="faq-question" v-on:click="onClick">
                {{ question }}
            </a>
        </summary>

        <div class="faq-answer">
            <slot></slot>
        </div>
    </details>
</template>

<style>
a.faq-question {
    color: inherit;
}

a.faq-question:hover {
    text-decoration: none;
}

.faq-entry {
    margin: 16px 0;
    color: var(--vp-custom-block-details-text);
    background-color: var(--vp-custom-block-details-bg);
    transition: 0.3s;

    border: 1px solid var(--vp-custom-block-details-border);
    border-radius: 8px;
    scroll-margin-top: -100px;
}

.faq-entry summary {
    display: inline;
    margin: 0;
}

.faq-question {
    display: list-item;
    font-size: 20px;
    cursor: pointer;
    transition: 0.1s;
    padding: 16px 20px;
}

.faq-question:hover {
    color: var(--vp-c-text-1);
}

.faq-answer {
    padding: 0 20px;
}

.faq-answer> :first-child {
    margin-top: 0;
}

.faq-entry[open] {
    color: var(--vp-c-text-1);
    border-color: var(--vp-custom-block-tip-border);
}
</style>