import { createMemoryHistory, createRouter } from 'vue-router'

import ChatView from '../ChatView.vue'
import AboutView from '../AboutView.vue'

const routes = [
  { path: '/', component: ChatView },
  { path: '/about', component: AboutView },
]

export const router = createRouter({
  history: createMemoryHistory(),
  routes,
})
