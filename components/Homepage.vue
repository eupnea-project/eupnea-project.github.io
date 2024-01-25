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
                    Boot a full Linux system and gain complete control over your device WITHOUT modifying the firmware.
                </b></p>
            <p class="fade-in-light"><b>
                    Note from the developer(s):</b> This project is officially dead and/or unmaintained(Though if I know Apacelus right he would revive it for the ten billionth time in a row in a month or so). 
                </p>
            <h2 class="fade-in-light"><b>
                   Use these projects instead:</b>
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
                        With the help of MrChromebox's firmware script, we can run Coreboot(UEFI) on our chromebooks, allowing it to be used like a regular 'laptop'. Supported devices are <a href="https://mrchromebox.tech/#devices">here</a>.
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
                        A product of Fyra labs, Submarine is a small linux environment that fits on a ChromeOS kernel partition. It's used to boot a full linux distro.
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
