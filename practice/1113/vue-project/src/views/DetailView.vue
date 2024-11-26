<template>
  <div>
    <h1>Detail</h1>
    <div v-if="article">
      <p>글번호 : {{ article.id }}</p>
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <p>작성시간 : {{ article.created_at }}</p>
      <p>수정시간 : {{ article.updated_at }}</p>
      <p>{{ a }}</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()
const route = useRoute()
// 단일 게시글은 배열이 아닌 null값으로 초기화
const article = ref(null)
const a = route.params.title
// DetailView가 마운트 되기 전에 요청 후 응답 데이터를 article에 저장
onMounted(() => {
  axios({
    method: 'get',
    // ArticleListItem의 params
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
  })
    .then((res) => {
      article.value = res.data
    })
    .catch(err => console.log(err))
})

</script>

<style>

</style>
