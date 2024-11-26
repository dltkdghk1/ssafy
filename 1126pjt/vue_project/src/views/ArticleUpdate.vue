<template>
  <div>
      <h1>게시글 수정</h1>
      <form @submit.prevent="updateArticle">
          <!-- 제목 입력 필드 -->
          <label for="title">제목 : </label>
          <input type="text" id="title" v-model.trim="title"><br>
    
          <!-- 내용 입력 필드 -->
          <label for="content">내용 : </label>
          <textarea name="content" v-model.trim="content"></textarea><br>

          <!-- 등록 버튼 -->
          <input type="submit" value="등록">
      </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from '../services/axios';

const route = useRoute(); // 현재 라우트 정보 가져오기
const title = ref(''); // 제목을 저장할 변수
const content = ref(''); // 내용을 저장할 변수
const router = useRouter()

// 게시글 데이터를 가져오는 함수
onMounted(async () => {
try {
  // API 호출로 게시글 데이터 가져오기
  const response = await axios.get(`http://127.0.0.1:8000/api/v1/articles/${route.params.id}/`);
  title.value = response.data.title; // 제목 초기값 설정
  content.value = response.data.content; // 내용 초기값 설정
} catch (error) {
  console.error('게시글을 가져오는 데 실패했습니다:', error.response?.data || error.message);
}
});

// 게시글 수정 함수
const updateArticle = async () => {
try {
  // API 호출로 게시글 수정 요청
  await axios.put(`http://127.0.0.1:8000/api/v1/articles/${route.params.id}/`, {
    title: title.value,
    content: content.value,
  });
  alert('게시글이 성공적으로 수정되었습니다.');
  router.push({ name: 'detail', params: { id: route.params.id } });
} catch (error) {
  console.error('게시글 수정에 실패했습니다:', error.response?.data || error.message);
}
};
</script>
