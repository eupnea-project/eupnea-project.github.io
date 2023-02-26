<script setup>
import Homepage from "./homepage.vue";
</script>

<template>
    <div id="home">
        <Homepage />
    </div>
</template>

<style scoped>
#home {
    width: 100%;
    height: 100%;
    padding: 0;
    box-sizing: border-box;
    background-color: var(--base-background-contrast);
    color: var(--base-color);
    font-family: var(--base-font-family);
    font-size: 1.5rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    line-height: normal;
    --content-width: 85rem;
}
</style>