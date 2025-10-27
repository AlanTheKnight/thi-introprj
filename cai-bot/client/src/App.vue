<script setup lang="ts">
import MainNav from "./MainNav.vue"
import logo from "@/assets/chat.png"
import Chat from './Chat.vue'
</script>

<template>
  <div class="border-b">
    <div class="flex h-16 items-center px-4">

      <img :src="logo" id="logo"/>
     
      <MainNav class="mx-6" />
      <div class="ml-auto flex items-center space-x-4">
      
      </div>
    </div>
  </div>

  <Chat/>
</template>

<style scoped>
#logo {
  width: 40px;
  height: 40px;
}
</style>

