<script setup lang="ts">
import MainNav from './MainNav.vue'
import logo from '@/assets/chat.png'
import Chat from './Chat.vue'
</script>

<template>
  <div class="flex flex-col h-[100vh]" id="app-container">
    <div class="">
      <div
        class="flex flex-row h-16 items-center px-4 w-full border-grid sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60"
      >
        <img :src="logo" id="logo" />

        <MainNav class="mx-6" />

        <div class="ml-auto flex items-center space-x-4"></div>
      </div>
    </div>

    <Chat />
  </div>
</template>

<style scoped>
#logo {
  width: 35px;
  height: 35px;
}

#app-container {
  background-image: linear-gradient(to top, #c8c7ffaa 0%, #dec9ce92 100%);
}
</style>
