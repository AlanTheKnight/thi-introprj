<script setup lang="ts">
import { ref } from 'vue'
import Button from './components/ui/button/Button.vue'

interface Message {
  text: string
  sender: 'user' | 'bot'
}

const messages = ref<Message[]>([])
const inputMessage = ref('')

function sendMessage() {
  if (!inputMessage.value.trim()) return

  // Add user's message
  messages.value.push({ text: inputMessage.value, sender: 'user' })

  // Simulate bot reply (replace with API call later)
  setTimeout(() => {
    messages.value.push({
      text: 'This is a response to: ' + inputMessage.value,
      sender: 'bot',
    })
  }, 500)

  inputMessage.value = ''
}
</script>

<template>
  <div class="flex flex-col h-[500px] w-full border rounded-lg overflow-hidden">
    <!-- Messages area -->
    <div class="flex-1 p-4 overflow-y-auto space-y-2 bg-gray-50">
      <div
        v-for="(msg, index) in messages"
        :key="index"
        :class="msg.sender === 'user' ? 'text-right' : 'text-left'"
      >
        <div
          :class="[
            'inline-block px-4 py-2 rounded-lg max-w-xs',
            msg.sender === 'user' ? 'bg-blue-500 text-white' : 'bg-gray-200 text-gray-800',
          ]"
        >
          {{ msg.text }}
        </div>
      </div>
    </div>

    <!-- Input area -->
    <div class="flex justify-center p-2 border-t">
      <div class="flex w-full max-w-md">
        <input
          v-model="inputMessage"
          @keyup.enter="sendMessage"
          type="text"
          placeholder="Type your question..."
          class="flex-1 px-4 py-2 rounded-full bg-gray-200/80 text-black border-none focus:outline-none"
        />
        <Button @click="sendMessage">Send</Button>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Optional: scroll to bottom when new message comes in */
</style>
