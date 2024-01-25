<script setup>
import Chevron from "./Chevron.vue";
</script>

<template>
    <section class="full-height initial-view">
        <div id="heading">
            <h1>
                <b style="color: var(--eupnea-green);">Your </b>
                <b style="color: var(--eupnea-blue);">Chromebook</b><b style="color: var(--eupnea-green);">, your way</b>
            </h1>
            <p class="fade-in-light"><b>
                    The Eupnea Project has beeen discontinued.
                </b></p>
            <h2 class="fade-in-light"><b>
                   Please use one of these projects instead:</b>
            </h2>
        </div>
        <div class="row fade-in">
            <div class="presentation" style="animation-delay: 0.2s;">
                <div class="extend">
                    <span class="title icon-text">
                    <img src="/assets/coreboot-icon.png" alt="Coreboot Logo">
                        <h2>Coreboot</h2>
                    </span>
                    <p>
                        MrChromebox's UEFI/RW_L (turn chromebook into almost a normal laptop):
                    </p>
                    <a href="https://mrchromebox.tech/#fwscript">
                        <button class="big solid">Link</button>
                    </a>
                </div>
            </div>
            <div class="separator no-fade"></div>
            <div class="presentation" style="animation-delay: 0.4s;">
                <div class="extend">
                    <span class="title icon-text">
                    <img src="/assets/fyra-labs.png" alt="Fyra Labs logo">
                        <h2>Submarine</h2>
                    </span>
                    <p>
                        FyraLab's submarine (does not require firmware modification)
                    </p>
                    <a href="https://github.com/FyraLabs/submarine">
                        <button class="big solid">Link</button>
                    </a>
                </div>
            </div>
        </div>
    </section>
    
    <p></p>
    <a href="old-page">Go to Old Page</a>
    <p></p>

    <small>
        hi milky. also apple sauce...fuck you!
    </small>

    <footer>
        &copy; 2024 The Eupnea Project 
    </footer>
</template>

<style scoped>
@import url(style/homepage.css);
</style>
