import { createRouter, createWebHistory } from 'vue-router'
import MovieHome from '@/views/MovieHome.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'moviehome',
      component: MovieHome
    },
  ],
})

export default router
