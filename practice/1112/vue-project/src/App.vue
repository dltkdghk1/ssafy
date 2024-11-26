<template>
  <h1>게시판</h1>
  <h2>완료된 할일 : {{ store.doneTodoCount }}</h2>

  <TodoList />
  <TodoForm />
</template>


<script setup>
  // 1. 중앙저장소(counter.js) 가져오기
  import { useCounterStore } from '@/stores/counter'
  
  import TodoForm from '@/components/TodoForm.vue'
  import TodoList from '@/components/TodoList.vue'
  
  const store = useCounterStore()

</script>



<style scoped>

</style>
