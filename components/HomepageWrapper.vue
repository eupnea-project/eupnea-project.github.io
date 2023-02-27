<script setup>
import Homepage from "./Homepage.vue";
</script>

<template>
    <div id="home">
        <Homepage />
    </div>
</template>

<style scoped>
#home {
    padding: 0;
    box-sizing: border-box;
    background-color: var(--base-background-contrast);
    color: var(--base-color);
    font-family: var(--base-font-family);
    font-size: 1rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    line-height: normal;
    --content-width: 85rem;
}

@media screen and (max-width: 799px) {
    #home {
        font-size: 0.8rem;
    }
}

@media screen and (min-width: 2000px) {
    #home {
        font-size: 1.1rem;
    }
}
</style>