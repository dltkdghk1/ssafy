<template>
  <div class="container">
    <nav class="top-nav">
      <div class="nav-left">
        <button @click="goToShortsPage">Watch Movie Shorts</button>
        <button @click="goToCommunity">Community</button>
      </div>
      <div class="nav-right">
        <button v-if="!isAuthenticated" @click="goToLoginPage">Login</button>
        <button v-else @click="handleLogout">Logout</button>
        <button @click="goToMyPage">My Page</button>
      </div>
    </nav>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';

export default {
  name: 'HomePage',
  setup() {
    const store = useStore();
    const router = useRouter();
    const isAuthenticated = computed(() => store.getters.isAuthenticated);

    const goToShortsPage = () => {
      if (!isAuthenticated.value) {
        console.error('토큰이 없습니다. 로그인을 먼저 해주세요.');
        router.push({ name: 'Login' });
        return;
      }
      router.push({ name: 'ShortsPage' });
    };

    const goToLoginPage = () => {
      router.push({ name: 'Login' });
    };

    const handleLogout = () => {
      store.dispatch('logout');
      router.push({ name: 'HomePage' });
    };

    const goToCommunity = () => {
      router.push({ name: 'community' })
    }

    const goToMyPage = () => {
      router.push({ name: 'user' })
    }

    return {
      goToShortsPage,
      goToLoginPage,
      handleLogout,
      isAuthenticated,
      goToCommunity,
      goToMyPage
    };
  },
};
</script>

<style scoped>
.container {
  text-align: center;
  position: relative;
  max-width: 800px;
  margin: 0 auto;
}

.top-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background-color: #333;
  color: #fff;
}

.nav-left,
.nav-right {
  display: flex;
  gap: 10px;
}

button {
  padding: 10px 20px;
  background-color: #4caf50;
  color: white;
  border: none;
  cursor: pointer;
}

button.disabled {
  background-color: #aaa;
  cursor: not-allowed;
}
</style>
