import { createRouter, createWebHistory } from 'vue-router'
import Starwars from '../components/Starwars.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/starwars',
      name: 'starwars',
      component: Starwars
    },
  ]
})

export default router
