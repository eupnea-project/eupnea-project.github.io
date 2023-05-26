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
        </div>
        <div class="row fade-in">
            
            <div class="presentation" style="animation-delay: 0.4s;">
                <div class="extend">
                    <span class="title icon-text">
                        <img src="/assets/depthboot-icon.png" alt="Depthboot Logo">
                        <h2>Depthboot</h2>
                    </span>
                    <p>
                        <b>Choose</b> between a variety of <b>common Linux distributions</b> and <b>desktop environments</b>
                        to create a bootable image for
                        <a href="docs/project/supported-devices">supported 64-bit Chromebooks.</a>
                    </p>
                    <a href="docs/depthboot/requirements" tabindex="-1">
                        <button class="big solid">Build now</button>
                    </a>
                </div>
                <ul class="soft logo-grid">
                    <li class="icon-text"><img src="/assets/distro-ubuntu.svg" draggable="false">Ubuntu</li>
                    <li class="icon-text"><img src="/assets/distro-fedora.png" draggable="false">Fedora</li>
                    <li class="icon-text"><img src="/assets/distro-popos.svg" draggable="false">Pop!_OS</li>
                    <li class="icon-text"><img src="/assets/distro-arch.svg" draggable="false">Arch Linux</li>
                </ul>
            </div>
        </div>
        <div class="row fade-in">
            <!-- <a href="overview" tabindex="-1" style="animation-delay: 0.6s;">
                <button class="big outline">Documentation</button>
            </a> -->
            <a href="faq" tabindex="-1" style="animation-delay: 0.5s;">
                <button class="big outline">Read the <b>FAQ</b></button>
            </a>
        </div>
        
    </section>

    <footer>
        &copy; 2023 The Eupnea Project
    </footer>
</template>

<style scoped>
@import url(style/homepage.css);
</style>
