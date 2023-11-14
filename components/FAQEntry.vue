<script setup>
import slugify from "@sindresorhus/slugify";
import { ref, onMounted } from "vue";

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
const entryRef = ref();

function scrollToEntry() {
    const element = entryRef.value;
    const questionElement = element.querySelector(".faq-question");
    const rect = questionElement.getBoundingClientRect();

    const yPosition = window.scrollY + rect.top - (window.innerHeight / 2 - rect.height / 2);
    const adjustedPosition = Math.min(Math.max(yPosition, 0), document.documentElement.scrollHeight - window.innerHeight);

    window.scrollTo({
        top: adjustedPosition,
        duration: 1000
        behavior: "smooth"
    });
}

function checkIsActive() {
    const hash = window.location.hash;
    const isActive = hash.substring(1) === myHash;

    if (isActive) {
        isOpen.value = true;
        scrollToEntry();
    }
}

function onClick(ev) {
    ev.preventDefault();
    ev.stopPropagation();

    isOpen.value = !isOpen.value;

    if (isOpen.value) {
        // Update anchor hash
        const href = new URL(window.location.href);
        href.hash = myHash;
        window.history.replaceState({}, "", href);

        scrollToEntry();
    }
}


onMounted(() => {
    if (window.location.hash) {
        checkIsActive();
        scrollToEntry();
    }
});
</script>

<template>
    <details class="faq-entry" :open="isOpen" :id="myHash" ref="entryRef">
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
