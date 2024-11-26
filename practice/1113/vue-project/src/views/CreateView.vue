<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <!-- 양방향 바인딩 v-model.trim : 공백 제거 -->
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" v-model.trim="content"></textarea> <br>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
  import axios from 'axios'
  import { ref } from 'vue'
  import { useCounterStore } from '@/stores/counter';
  import { useRouter } from 'vue-router';

  const store = useCounterStore()
  const router = useRouter()

  const title = ref(null)
  const content = ref(null)

  // 제출 버튼을 누르면 createArticle 함수가 실행되게
  const createArticle = function () {
    axios ({
      method: 'post',
      url: `${store.API_URL}/api/v1/articles/`,
      data: {
        title: title.value,
        content: content.value
      }
    })
      .then(() => {
        // create 완료 후에 메인페이지로 리다이렉트
        router.push({ name: 'ArticleView'})
      })
      .catch(err => console.log(err))
  }

</script>

<style>

</style>
