import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '../views/UserView.vue'
import UserHome from '@/components/UserHome.vue'
import UserProfile from '@/components/UserProfile.vue'
import UserPosts from '@/components/UserPosts.vue'
import LoginView from '@/views/LoginView.vue'

const isAuthenticated = true

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/', // url
      name: 'home', // 라우트 name
      component: HomeView, // 해당 경로에서 보여줄 컴포넌트
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/user/:id',
      name: 'user',
      // views 디렉토리
      component: UserView,
      // beforEach: 전역가드(모든 라우트 이동에서 실행)
      // beforenter: 특정 라우트 가드(특정 라우트 이동에서만 실행)
      beforeEnter: (to, from) => {
        console.log(to) // 이동할 라우트
        console.log(from) // 이동전 라우트
      },

      // 중첩 라우트
      children: [
        {path: '', name: 'user', component: UserHome}, // localhost/user/:id
        {path: 'profile', name: 'user-profile', component: UserProfile}, // localhost/user/:id/profile
        {path: 'posts', name: 'user-posts', component: UserPosts} // localhost/user/:id/posts
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      beforeEnter: (to, from) => {
        if (isAuthenticated === true) {
          console.log('이미 로그인한 상태입니다.')
          return { name: 'home' } // 이미 로그인된 상태라면 홈으로 리다이렉트
        }
      }
    }
  ],
})

export default router
