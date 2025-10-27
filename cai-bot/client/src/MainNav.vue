<template>
  <nav class="flex flex-row w-full items-center">
    <!-- Navigation links -->
    <div class="flex flex-1 space-x-4 lg:space-x-6">
      <a href="/" class="text-sm font-medium hover:text-primary">Chat</a>
      <a href="/about" class="text-sm font-medium text-gray-400 hover:text-primary">
        About
      </a>
    </div>

    <Avatar>
      <AvatarImage :src="userImg" />
      <AvatarFallback>CN</AvatarFallback>
    </Avatar>
  </nav>
</template>

<script setup lang="ts">
import Avatar from './components/ui/avatar/Avatar.vue'
import AvatarImage from './components/ui/avatar/AvatarImage.vue'
import AvatarFallback from './components/ui/avatar/AvatarFallback.vue'
import userImg from '@/assets/user.svg'
</script>
