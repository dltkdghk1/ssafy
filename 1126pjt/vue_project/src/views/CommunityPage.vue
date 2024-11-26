<template>
  <div class="community-page">
    <header class="header">
      <h1>커뮤니티</h1>
      <div class="button-group">
        <button class="nav-button" @click="goToHome">홈으로</button>
        <button class="nav-button" @click="goToMakeArticle">게시글 생성</button>
      </div>
    </header>
    
    <section class="articles-section">
      <div v-if="articles.length > 0" class="articles-list">
        <ArticleList 
          v-for="article in articles"
          :key="article.id"
          :article="article"
        />
      </div>
      <div v-else class="no-articles">
        <p>아직 게시글이 없습니다. 게시글을 생성해보세요!</p>
      </div>
    </section>
  </div>
</template>

<script setup>
import axios from '../services/axios';
import ArticleList from '../components/ArticleList.vue';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

const articles = ref([]);
const router = useRouter();

onMounted(() => {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/articles/',
  })
    .then((res) => {
      articles.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
});

const goToMakeArticle = function () {
  router.push({ name: 'articlemake' });
};

const goToHome = function () {
  router.push({ name: 'ShortsPage' });
};
</script>

<style scoped>
/* 전체 페이지 스타일 */
.community-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Arial', sans-serif;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

/* 헤더 스타일 */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 20px;
  border-bottom: 2px solid #ddd;
  margin-bottom: 20px;
}

.header h1 {
  font-size: 2rem;
  color: #333;
}

.button-group {
  display: flex;
  gap: 15px;
}

.nav-button {
  background-color: #ff5f6d;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.3s, transform 0.2s;
}

.nav-button:hover {
  background-color: #e14a55;
  transform: scale(1.05);
}

/* 게시글 리스트 스타일 */
.articles-section {
  background: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.articles-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.no-articles {
  text-align: center;
  font-size: 1.2rem;
  color: #777;
}
</style>
