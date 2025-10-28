<template>
  <nav class="flex flex-row w-full items-center gap-5">
    <!-- Navigation links -->
    <div class="flex flex-1 space-x-4 lg:space-x-6">
      <RouterLink
        to="/"
        class="text-sm font-medium hover:text-primary"
        :class="{
          'text-primary': $route.path === '/',
          'text-gray-400': $route.path !== '/',
        }"
        >Chat</RouterLink
      >
      <RouterLink
        to="/about"
        class="text-sm font-medium hover:text-primary"
        :class="{
          'text-primary': $route.path === '/about',
          'text-gray-400': $route.path !== '/about',
        }"
      >
        About
      </RouterLink>
    </div>

    <DropdownMenu>
      <DropdownMenuTrigger as-child>
        <Button variant="outline" size="sm">
          <MoonIcon
            class="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0"
          />
          <SunIcon
            class="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100"
          />
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        <DropdownMenuItem @click="mode = 'light'"> Light </DropdownMenuItem>
        <DropdownMenuItem @click="mode = 'dark'"> Dark </DropdownMenuItem>
        <DropdownMenuItem @click="mode = 'auto'"> System </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>

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
import { RouterLink } from 'vue-router'
import { MoonIcon, SunIcon } from 'lucide-vue-next'
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'
import Button from '@/components/ui/button/Button.vue'

import { useColorMode } from '@vueuse/core'

const mode = useColorMode()
</script>
