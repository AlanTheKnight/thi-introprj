<template>
  <nav class="flex items-center space-x-4 lg:space-x-6">
    <!-- Navigation links -->
    <a href="/examples/dashboard" class="text-sm font-medium hover:text-primary">
      Overview
    </a>
    <a href="/examples/dashboard" class="text-sm font-medium text-gray-400 hover:text-primary">
      Customers
    </a>
    <a href="/examples/dashboard" class="text-sm font-medium text-gray-400 hover:text-primary">
      Products
    </a>
    <a href="/examples/dashboard" class="text-sm font-medium text-gray-400 hover:text-primary">
      Settings
    </a>

    <!-- Profile picture aligned to the right -->
    <div class="ml-auto">
      <img
        :src="profilePic"
        alt="User Profile"
        class="w-10 h-10 rounded-full border-2 border-gray-300"
      />
    </div>
  </nav>
</template>

<script setup lang="ts">
const profilePic = 'https://i.pravatar.cc/40' // placeholder avatar
</script>
