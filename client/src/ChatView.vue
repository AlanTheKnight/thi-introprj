<template>
  <div>
    <div class="flex flex-col" id="chat-wrapper-container">
      <Chat />
    </div>
  </div>
</template>

<script lang="ts" setup>
import Chat from './components/Chat.vue'
</script>

<style>
#chat-wrapper-container {
  height: calc(100vh - 64px);
}
</style>
