<template>
  <div>
    <MovieListItem 
      v-for="movie in store.movies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script setup>
import MovieListItem from './MovieListItem.vue';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()


</script>

<style scoped>

</style>