<template>
    <div>
        <!-- <form @submit.prevent="store.addTodo(todoText)" ref="formElem"> -->
        <form @submit.prevent="createTodo(todoText)" ref="formElem">
            <input type="text" v-model="todoText">
            <input type="submit">
        </form>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref } from 'vue'

const store = useCounterStore()
const todoText = ref('')

// form태그 선택
const formElem = ref(null)

// 중앙 저장소의 addTodo 액션을 직접 호출해도 되지만ㄴ
// 굳이 createTodo를 만들어서 호춯하는 이유는 
// addTodo호출 전후로 추가 로직을 작성할 수 있기 때문이다
const createTodo = function (todoText) {
    store.addTodo(todoText)
    formElem.value.reset()
}

</script>

<style scoped>

</style>