<!-- views/SignUpView.vue -->

<template>
  <div>
    <h1>회원가입 페이지</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <!-- 양방향 바인딩, 공백제거 -->
      <input type="text" id="username" v-model.trim="username" autocomplete="new-username"><br>

      <label for="password1">password : </label>
      <input type="password" id="password1" v-model.trim="password1" autocomplete="new-password"><br>

      <label for="password2">password confirm : </label>
      <input type="password" id="password2" v-model.trim="password2" autocomplete="new-password"><br>

      <input type="submit" value="Signup">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

// form을 제출하면 signUp함수가 호출
const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  store.signUp(payload)
}

</script>

<style>

</style>
