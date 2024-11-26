import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import ShortsPage from '../views/ShortsPage.vue';
import LoginPage from '../views/LoginPage.vue';
import SignupPage from '../views/SignupPage.vue';
import CommunityPage from '../views/CommunityPage.vue';
import ArticleMakePage from '../views/ArticleMakePage.vue';
import ArticleDetail from '../views/ArticleDetail.vue';
import ArticleUpdate from '../views/ArticleUpdate.vue';
import UserPage from '../views/UserPage.vue';
import ChangePassword from '../views/ChangePassword.vue';

const routes = [
  {
    path: '/Home',
    name: 'HomePage',
    component: HomePage,
  },
  {
    path: '/',
    name: 'ShortsPage',
    component: ShortsPage,
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage,
  },
  {
    path: '/signup',
    name: 'Signup',
    component: SignupPage,
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityPage
  },
  {
    path: '/articlemake',
    name: 'articlemake',
    component: ArticleMakePage
  },
  {
    path: '/articles/:id',
    name: 'detail',
    component: ArticleDetail
  },
  {
    path: '/articleupdate/:id',
    name: 'update',
    component: ArticleUpdate
  },
  {
    path: '/user',
    name: 'user',
    component: UserPage
  },
  {
    path: '/password',
    name: 'password',
    component: ChangePassword
  },
  {
    path: '/watch-history',
    name: 'WatchHistoryPage',
    component: () => import('../views/WatchHistoryPage.vue')
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
