<script setup lang="ts">
import { ref } from 'vue'
import Button from '@/components/ui/button/Button.vue'
import Textarea from '@/components/ui/textarea/Textarea.vue'

interface Message {
  text: string
  sender: 'user' | 'bot'
}

const messages = ref<Message[]>([])
const inputMessage = ref('')

async function sendMessage() {
  if (!inputMessage.value.trim()) return

  messages.value.push({ text: inputMessage.value, sender: 'user' })

  const response = await fetch('/api/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ message: inputMessage.value }),
  })

  if (!response.ok) {
    console.error('Failed to send message')
    return
  }

  const data = await response.json()

  messages.value.push({ text: data.answer, sender: 'bot' })

  inputMessage.value = ''
}
</script>

<template>
  <div class="flex flex-1 flex-col h-[500px] w-full border overflow-hidden">
    <!-- Messages area -->
    <div class="flex-1 p-4 overflow-y-auto space-y-2" id="messages-container">
      <div
        v-for="(msg, index) in messages"
        :key="index"
        :class="msg.sender === 'user' ? 'text-right' : 'text-left'"
      >
        <div
          :class="[
            'inline-block px-4 py-2 rounded-lg max-w-xs',
            msg.sender === 'user' ? 'bg-violet-500 text-white' : 'bg-white text-gray-800',
          ]"
        >
          {{ msg.text }}
        </div>
      </div>
    </div>

    <!-- Input area -->
    <div class="flex justify-center p-5 border-t bg-white">
      <div class="flex w-full max-w-lg items-end gap-3">
        <Textarea
          v-model="inputMessage"
          @keyup.enter="sendMessage"
          placeholder="Type your question..."
          class="flex-1 px-4 py-2"
        />
        <Button @click="sendMessage">Send</Button>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
