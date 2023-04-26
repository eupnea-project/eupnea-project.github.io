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
            <div class="presentation" style="animation-delay: 0.2s;">
                <div class="extend">
                    <span class="title icon-text">
                        <img src="/assets/eupneaos-icon.png" alt="EupneaOS Logo">
                        <h2>EupneaOS</h2>
                    </span>
                    <p>
                        EupneaOS is a <a href="https://getfedora.org">Fedora</a> based operating system optimized to run on
                        <a href="docs/project/supported-devices">supported 64-bit
                            Chromebooks</a>. It features a custom (<a href="https://kde.org/">KDE</a> based)
                        <b>ChromeOS style desktop</b> and native <b>Android app support</b>.
                    </p>
                    <button class="big solid" disabled>Coming soon</button>
                </div>
                <p class="soft">
                    EupneaOS is still in development. Stay tuned.
                </p>
            </div>
            <div class="separator no-fade"></div>
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
        <Chevron />
    </section>

    <section class="bg-mute full-height info-row">
        <div class="blog">
            <h2>EupneaOS</h2>
            <p>
                The Eupnea Project develops a custom Linux distribution based on
                <a href="https://getfedora.org">Fedora</a> called <b>EupneaOS</b>. It's designed to imitate the
                look of ChromeOS and is the recommended way of upgrading your Chromebook. It is designed to replicate
                most features of ChromeOS, but without any limitations.
            </p>
            <p>
                Precompiled iso images are available on the
                <a href="https://github.com/eupnea-linux/eupneaos/releases">GitHub Releases</a>
                page and can be flashed directly to a USB stick or SD card.
            </p>
            <button class="big solid" disabled>Coming soon</button>
        </div>
        <div class="preview">
            <img class="big" src="https://via.placeholder.com/1280x720" alt="Placeholder Image">
            <img class="icon" style="left: -3vw; bottom: -2vh" src="/assets/eupneaos-icon.png">
        </div>
    </section>
    <section class="full-height info-row rev-row">
        <div class="blog">
            <h2>Depthboot</h2>
            <p>
                <b>Depthboot</b> (a fork of <a href="https://github.com/cb-linux/breath" target="_blank"
                    rel="noopener noreferrer">Breath</a>) can create bootable images for all
                64-bit Chromebooks. Multiple
                Linux distributions and desktop environments are supported.
            </p>
            <p>
                Follow the instructions described in the documentation to build a Depthboot image.
            </p>
            <a href="docs/depthboot/requirements" tabindex="-1">
                <button class="big solid">Build instructions</button>
            </a>
        </div>
        <div class="preview">
            <img class="big" src="https://via.placeholder.com/1280x900" alt="Placeholder Image">
            <img class="icon" style="right: -2vw; top: -3vh; animation-delay: 2s;" src="/assets/depthboot-icon.png">
        </div>
    </section>

    <footer>
        &copy; 2023 The Eupnea Project
    </footer>
</template>

<style scoped>
@import url(style/homepage.css);
</style>
