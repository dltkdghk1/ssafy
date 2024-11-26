<!-- src/views/WatchHistoryPage.vue -->
<template>
  <div class="watch-history-container">
    <h2>Your Watch History</h2>
    <div v-if="watchHistory.length > 0">
      <div v-for="history in watchHistory" :key="history.id" class="history-item">
        <h3>{{ history.movie.title }}</h3>
        <p><strong>Genre:</strong> {{ history.genre_names }}</p>
        <p><strong>Watched Percentage:</strong> {{ history.watched_percentage }}%</p>
        <p><strong>Watched At:</strong> {{ formatDate(history.watched_at) }}</p>
      </div>
    </div>
    <div v-else>
      <p>No watch history available yet.</p>
    </div>
    <div class="back-home-button">
      <button @click="goToHomePage">Back to HomePage</button>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from '../services/axios'; // axios 설정 파일 사용
import { useRouter } from 'vue-router';

export default {
  name: 'WatchHistoryPage',
  setup() {
    const watchHistory = ref([]);
    const router = useRouter();

    onMounted(async () => {
      try {
        const response = await axios.get('/accounts/watch-history/');
        watchHistory.value = response.data;
      } catch (error) {
        console.error('Failed to fetch watch history:', error);
      }
    });

    const formatDate = (dateString) => {
      const options = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' };
      return new Date(dateString).toLocaleDateString('en-US', options);
    };

    const goToHomePage = () => {
      router.push({ name: 'HomePage' });
    };

    return {
      watchHistory,
      formatDate,
      goToHomePage,
    };
  },
};
</script>

<style scoped>
.watch-history-container {
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}

.history-item {
  border: 1px solid #ddd;
  padding: 20px;
  margin: 20px 0;
  text-align: left;
}

.back-home-button {
  margin-top: 20px;
}

.back-home-button button {
  padding: 10px 20px;
  background-color: #4caf50;
  color: white;
  border: none;
  cursor: pointer;
  font-size: 16px;
}

.back-home-button button:hover {
  background-color: #45a049;
}
</style>
