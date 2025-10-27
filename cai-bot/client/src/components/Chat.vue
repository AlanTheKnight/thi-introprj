<script setup lang="ts">
import { ref, onMounted, watch, nextTick } from 'vue'
import Button from '@/components/ui/button/Button.vue'
import Textarea from '@/components/ui/textarea/Textarea.vue'

interface Message {
  text: string
  sender: 'user' | 'bot'
}

const messages = ref<Message[]>([])
const inputMessage = ref('')

// LocalStorage key for storing messages
const STORAGE_KEY = 'chat-messages'

// Function to save messages to localStorage
function saveMessages() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(messages.value))
  } catch (error) {
    console.error('Failed to save messages to localStorage:', error)
  }
}

// Function to load messages from localStorage
function loadMessages() {
  try {
    const storedMessages = localStorage.getItem(STORAGE_KEY)
    if (storedMessages) {
      const parsedMessages = JSON.parse(storedMessages)
      if (Array.isArray(parsedMessages)) {
        messages.value = parsedMessages
      }
    }
  } catch (error) {
    console.error('Failed to load messages from localStorage:', error)
  }
}

// Load messages when component mounts
onMounted(() => {
  loadMessages()
  scrollToBottom()
})

// Watch for changes in messages and save to localStorage
watch(messages, saveMessages, { deep: true })

// Function to scroll to bottom of messages
function scrollToBottom() {
  nextTick(() => {
    const container = document.getElementById('messages-container')
    if (container) {
      container.scrollTop = container.scrollHeight
    }
  })
}

// Function to clear all messages
function clearMessages() {
  messages.value = []
  localStorage.removeItem(STORAGE_KEY)
}

async function sendMessage() {
  if (!inputMessage.value.trim()) return

  messages.value.push({ text: inputMessage.value, sender: 'user' })
  scrollToBottom()

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
  scrollToBottom()

  inputMessage.value = ''
}
</script>

<template>
  <div class="flex flex-1 flex-col h-[500px] w-full border overflow-hidden">
    <!-- Header with clear button -->
    <div
      class="flex justify-between items-center p-3 border-b bg-white"
    >
      <h3 class="text-lg font-medium text-gray-700">Charlie Chatbot</h3>
      <Button v-if="messages.length > 0" @click="clearMessages" variant="outline" size="sm">
        Clear Chat
      </Button>
    </div>

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
