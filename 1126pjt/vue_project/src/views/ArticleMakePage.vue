<template>
  <div class="make-article-page">
    <header class="header">
      <h1>게시글 작성</h1>
    </header>
    <form @submit.prevent="makeArticle" class="article-form">
      <div class="form-group">
        <label for="title" class="form-label">제목:</label>
        <input type="text" id="title" v-model.trim="title" class="form-input" placeholder="제목을 입력하세요">
      </div>

      <div class="form-group">
        <label for="content" class="form-label">내용:</label>
        <textarea id="content" v-model.trim="content" class="form-textarea" placeholder="내용을 입력하세요"></textarea>
      </div>

      <div class="button-group">
        <input type="submit" value="등록" class="submit-button">
        <button @click="goToCommunity" type="button" class="cancel-button">취소</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from '../services/axios';

const router = useRouter();
const title = ref('');
const content = ref('');

const makeArticle = function () {
  if (!title.value || !content.value) {
    alert('모든 필드를 채워주세요.');
    return;
  }

  axios({
    method: 'post',
    url: 'http://127.0.0.1:8000/api/v1/articles/',
    data: {
      title: title.value,
      content: content.value,
    },
  })
    .then((res) => {
      alert('등록되었습니다.');
      router.push({ name: 'community' });
    })
    .catch((err) => {
      console.error(err);
      alert('오류가 발생했습니다. 다시 시도해주세요.');
    });
};

const goToCommunity = () => {
  router.push({ name: 'community' });
};
</script>

<style scoped>
/* 전체 페이지 스타일 */
.make-article-page {
  max-width: 800px;
  margin: 40px auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  font-family: 'Arial', sans-serif;
}

/* 헤더 스타일 */
.header {
  text-align: center;
  margin-bottom: 30px;
}

.header h1 {
  font-size: 2rem;
  color: #333;
}

/* 폼 스타일 */
.article-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

/* 폼 그룹 */
.form-group {
  display: flex;
  flex-direction: column;
}

.form-label {
  font-weight: bold;
  margin-bottom: 5px;
  color: #555;
}

.form-input {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1rem;
}

.form-textarea {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1rem;
  height: 150px;
}

/* 버튼 그룹 스타일 */
.button-group {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* 제출 버튼 스타일 */
.submit-button {
  background-color: #ff5f6d;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
  transition: background 0.3s, transform 0.2s;
}

.submit-button:hover {
  background-color: #e14a55;
  transform: scale(1.05);
}

/* 취소 버튼 스타일 */
.cancel-button {
  background-color: #ccc;
  color: #333;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
  transition: background 0.3s, transform 0.2s;
}

.cancel-button:hover {
  background-color: #aaa;
  transform: scale(1.05);
}
</style>
