<template>
  <div class="article-page">
    <div class="article-detail">
      <p class="article-id">ID: {{ article.id }}</p>
      <h1 class="article-title">{{ article.title }}</h1>
      <p class="article-content">{{ article.content }}</p>
      
      <div class="button-group">
        <RouterLink :to="{ name: 'update', params: { id: route.params.id } }" class="edit-button">수정</RouterLink>
        <button @click="deleteArticle(article.id)" class="delete-button">삭제</button>
      </div>
    </div>

    <hr class="divider">

    <div class="comment-section">
      <h3>댓글</h3>
      <form @submit.prevent="makeComment" class="comment-form">
        <input type="text" id="comment" v-model.trim="content" class="comment-input" placeholder="댓글을 입력하세요">
        <input type="submit" value="등록" class="submit-button">
      </form>

      <ul class="comment-list">
        <li v-for="comment in article.comment_set" :key="comment.id" class="comment-item">
          <p class="comment-content">{{ comment.content }}</p>
          <button @click="deleteComment(comment.id)" class="delete-comment-button">삭제</button>
        </li>
      </ul>
    </div>

    <button @click="goToCommunity" class="back-button">뒤로가기</button>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { ref } from 'vue';
import axios from '../services/axios';
import { onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const article = ref([]);
const router = useRouter();
const content = ref('');

onMounted(() => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/articles/${route.params.id}/`,
  })
    .then((res) => {
      article.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
});

const goToCommunity = function () {
  router.push({ name: 'community' });
};

const makeComment = async function () {
  try {
    if (!content.value) {
      alert('댓글 내용을 입력해주세요.');
      return;
    }

    const response = await axios.post(
      `http://127.0.0.1:8000/api/v1/articles/${article.value.id}/comments/`,
      { content: content.value }
    );

    alert('댓글이 등록되었습니다.');
    content.value = ''; // 입력란 초기화
    article.value.comment_set.push(response.data); // 새 댓글 추가
  } catch (err) {
    console.error('Error:', err.response?.data || err.message);
  }
};

const deleteComment = function (commentId) {
  axios({
    method: 'delete',
    url: `http://127.0.0.1:8000/api/v1/comments/${commentId}/`,
  })
    .then((res) => {
      alert('댓글이 삭제되었습니다.');
      article.value.comment_set = article.value.comment_set.filter(comment => comment.id !== commentId);
    })
    .catch((err) => {
      console.log(err);
    });
};

const deleteArticle = function (articleId) {
  axios({
    method: 'delete',
    url: `http://127.0.0.1:8000/api/v1/articles/${articleId}/`,
  })
    .then((res) => {
      alert('게시글이 삭제되었습니다.');
      router.push({ name: 'community' });
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped>
/* 전체 페이지 스타일 */
.article-page {
  max-width: 800px;
  margin: 40px auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  font-family: 'Arial', sans-serif;
}

/* 게시글 상세 스타일 */
.article-detail {
  margin-bottom: 20px;
}

.article-id {
  font-size: 0.9rem;
  color: #888;
}

.article-title {
  font-size: 2rem;
  color: #333;
  margin: 15px 0;
}

.article-content {
  font-size: 1.1rem;
  color: #555;
}

/* 버튼 그룹 스타일 */
.button-group {
  display: flex;
  gap: 10px;
  margin-top: 20px;
}

.edit-button,
.delete-button {
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.3s, transform 0.2s;
}

.edit-button {
  background-color: #5f9ef5;
  color: white;
}

.edit-button:hover {
  background-color: #3b7bdc;
  transform: scale(1.05);
}

.delete-button {
  background-color: #ff5f6d;
  color: white;
}

.delete-button:hover {
  background-color: #e14a55;
  transform: scale(1.05);
}

/* 구분선 */
.divider {
  margin: 20px 0;
  border: 0;
  height: 1px;
  background: #ddd;
}

/* 댓글 섹션 스타일 */
.comment-section {
  margin-top: 20px;
}

.comment-form {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.comment-input {
  flex-grow: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1rem;
}

.submit-button {
  background-color: #5f9ef5;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
  transition: background 0.3s, transform 0.2s;
}

.submit-button:hover {
  background-color: #3b7bdc;
  transform: scale(1.05);
}

/* 댓글 리스트 */
.comment-list {
  list-style: none;
  padding: 0;
}

.comment-item {
  background: #f1f1f1;
  padding: 10px;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  margin-bottom: 15px;
}

.comment-content {
  margin: 0 0 10px 0;
  font-size: 1rem;
}

.delete-comment-button {
  background: #ff5f6d;
  color: #fff;
  border: none;
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: background 0.3s, transform 0.2s;
}

.delete-comment-button:hover {
  background: #e14a55;
  transform: scale(1.05);
}

/* 뒤로가기 버튼 */
.back-button {
  background-color: #ccc;
  color: #333;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
  transition: background 0.3s, transform 0.2s;
  margin-top: 20px;
}

.back-button:hover {
  background-color: #aaa;
  transform: scale(1.05);
}
</style>
