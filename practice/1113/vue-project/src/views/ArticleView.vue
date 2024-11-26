<template>
  <div>
    <h1>Articles</h1>

    <RouterLink :to="{ name:'CreateView' }">
      [CREATE]
    </RouterLink>
    
    <ArticleList />
  </div>
</template>

<script setup>
  import ArticleList from '@/components/ArticleList.vue';
  import { onMounted } from 'vue';
  import { useCounterStore } from '@/stores/counter';
  import { RouterLink } from 'vue-router';

  const store = useCounterStore()

  // ArticleView 컴포넌트가 마운트 될때 getArticles 함수가 실행
  onMounted(() => {
    store.getArticles()
  })


</script>

<style>

</style>
