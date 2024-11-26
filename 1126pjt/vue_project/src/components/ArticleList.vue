<template>
  <div>
    <h5>{{ article.title }}</h5>
    <p>{{ article.content }}</p>
    <RouterLink :to="{ name: 'detail', params:{ id: article.id } }">자세히</RouterLink>
    
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
;

defineProps({
  article: Object
})
</script>

<style scoped>

</style>