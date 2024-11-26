<template>
  <div>
    <h1>home</h1>
    <MovieList />
  </div>
</template>

<script setup>
import MovieList from '@/components/Movie/MovieList.vue';
import { onMounted, onUnmounted } from 'vue';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()

onMounted(() => {
  store.getMovies()
})
</script>

<style scoped>

</style>