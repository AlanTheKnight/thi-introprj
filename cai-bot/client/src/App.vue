<script setup lang="ts">
import MainNav from './MainNav.vue'
import logo from '@/assets/chat.png'
import { RouterView } from 'vue-router'
</script>

<template>
  <div class="bg-white dark:bg-slate-950 flex-1 h-full flex">
    <div class="flex-1" id="app-container">
      <div
        class="flex flex-row h-16 items-center px-4 w-full border-grid sticky top-0 z-50 bg-white dark:bg-slate-950 border-b"
      >
        <img :src="logo" id="logo" class="me-6" />

        <MainNav />

        <div class="ml-auto flex items-center space-x-4"></div>
      </div>

      <RouterView />
    </div>
  </div>
</template>

<style scoped>
#logo {
  width: 35px;
  height: 35px;
}

#app-container {
  background-image: linear-gradient(to top, #a18cd180 0%, #fbc2eb75 100%);
}

.dark #app-container {
  background-image: linear-gradient(to top, #a18cd12c 0%, #fbc2eb3a 100%);
}
</style>
