<script setup>
import "./style/homepage.css";
</script>

<template>
    <section class="full-height initial-view">
    <h1>
        <b style="color: var(--eupnea-green);">Your </b>
        <b style="color: var(--eupnea-blue);">Chromebook</b><b style="color: var(--eupnea-green);">, your way</b>
        <p>
            Boot a full Linux system and gain complete control over your device <b>WITHOUT</b> modifying the firmware.
        </p>
    </h1>
    <div class="row fade-in">
        <div class="presentation" style="animation-delay: 0.2s;">
            <div class="extend">
                    <span class="title">
                        <img src="assets/eupneaos_icon.png" alt="EupneaOS Logo">
                        <h2>EupneaOS</h2>
                    </span>
                <p>
                    EupneaOS is a <a href="https://getfedora.org">Fedora</a> based operating system optimized to run on
                    <a href="docs/extra/supported-devices">supported 64-bit
                        Chromebooks</a>. It features a custom (<a href="https://kde.org/">KDE</a> based)
                    <b>ChromeOS style desktop</b> and native <b>Android app support</b>.
                </p>
                <button class="big" disabled>Coming soon</button>
            </div>
            <p class="soft">
                EupneaOS is still in development. Stay tuned.
            </p>
        </div>
        <div class="separator"></div>
        <div class="presentation" style="animation-delay: 0.4s;">
            <div class="extend">
                    <span class="title">
                        <img src="assets/depthboot_icon.png" alt="Depthboot Logo">
                        <h2>Depthboot</h2>
                    </span>
                <p>
                    <b>Choose</b> between a variety of <b>common Linux distributions</b> and <b>desktop environments</b>
                    to create a bootable image for <a
                        href="docs/extra/supported-devices">supported 64-bit
                    Chromebooks.</a>
                </p>
                <a href="docs/depthboot/requirements" tabindex="-1">
                    <button class="big">Build now</button>
                </a>
            </div>
            <p class="soft logo-grid">
                <span><img src="assets/distro-ubuntu.svg" draggable="false">Ubuntu</span>
                <span><img src="assets/distro-fedora.png" draggable="false">Fedora</span>
                <span><img src="assets/distro-popos.svg" draggable="false">Pop!_OS</span>
                <span><img src="assets/distro-arch.svg" draggable="false">Arch Linux</span>
            </p>
        </div>
    </div>
    <svg class="chevron" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
        <path
                d="M233.4 406.6c12.5 12.5 32.8 12.5 45.3 0l192-192c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L256 338.7 86.6 169.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l192 192z"/>
    </svg>
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
        <button class="big" disabled>Coming soon</button>
    </div>
    <div class="preview">
        <img class="big" src="https://via.placeholder.com/1280x720" alt="Placeholder Image">
        <img class="icon" style="left: -3vw; bottom: -2vh" src="assets/eupneaos_icon.png">
    </div>
</section>
<section class="full-height info-row rev-row">
    <div class="blog">
        <h2>Depthboot</h2>
        <p>
            <b>Depthboot</b> (a fork of <a href="https://github.com/cb-linux/breath" target="_blank"
                                           rel="noopener noreferrer">Breath</a>) can create bootable images for all
            64-bit Chromebooks. Multiple
            Linux distributions and desktop environments are supported. <a
                href="https://docs.google.com/spreadsheets/d/1-zIX8lWEXVcO71xCuzvZpHvCUizrU7csKfJusqB2CYM"
                target="_blank" rel="noopener noreferrer">Full
            list of supported options</a>
        </p>
        <p>
            Follow the instructions described in the documentation to build a Depthboot image.
        </p>
        <a href="docs/depthboot/requirements" tabindex="-1">
            <button class="big">Build instructions</button>
        </a>
    </div>
    <div class="preview">
        <img class="big" src="https://via.placeholder.com/1280x900" alt="Placeholder Image">
        <img class="icon" style="right: -2vw; top: -3vh; animation-delay: 2s;" src="assets/depthboot_icon.png">
    </div>
</section>

<footer>
    &copy; 2023 The Eupnea Project
</footer>

<!-- <script src="index.js"></script> -->
</template>