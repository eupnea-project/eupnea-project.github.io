---
prev: false
next: false

title: Old Page
---

<template>
  <OldPage />
</template>

<script setup>
import OldPage from "/components/Oldpage.vue";
import Chevron from "/components/Chevron.vue";
</script>

<style scoped>
@import url(/components/style/homepage.css);
</style>

## Old Page

This page has info regarding the old Eupnea website page. 

It's in `/components/Oldpage.vue` on the repo, although cannot be rendered, as it's a `.vue`, not an `.md` or `.html` file, which can be rendered. The reason the homepage can be used is because it's an html template for the homepage.

However, I'm sure you(yes you Apacelus) can create an HTML file and import the CSS along with it. Though I wouldn't want to try something like that, it's not how the rest of the site is...