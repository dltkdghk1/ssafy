<template>
  <div class="signup-container">
    <div class="signup-card">
      <h1 class="signup-title">회원가입</h1>
      <form @submit.prevent="signUp()" class="signup-form">
        <div class="form-group">
          <label for="userid" class="form-label">회원ID</label>
          <input type="text" id="username" v-model.trim="username" class="form-input" placeholder="회원ID 입력">
        </div>

        <div class="form-group">
          <label for="password1" class="form-label">비밀번호</label>
          <input type="password" id="password1" v-model.trim="password1" class="form-input" placeholder="비밀번호 입력">
        </div>

        <div class="form-group">
          <label for="password2" class="form-label">비밀번호 확인</label>
          <input type="password" id="password2" v-model.trim="password2" class="form-input" placeholder="비밀번호 확인">
        </div>

        <button type="submit" class="signup-button">가입</button>
      </form>
      <p class="login-redirect">이미 계정이 있으신가요? <a @click="navigateToLogin" class="login-link">로그인</a></p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from '../services/axios';
import { useRouter } from 'vue-router';

const router = useRouter()
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const djangoSignUp = function (payload) {
  const username = payload.username
  const password1 = payload.password1
  const password2 = payload.password2

  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/signup/`,
    data: {
      username, password1, password2
    }
  })
    .then((res) => {
      alert('회원가입이 완료 되었습니다.')
      router.push({name: 'Login'}) 
    })
    .catch((err) => {
      console.log(err)
    })
}

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  djangoSignUp(payload)
}

const navigateToLogin = () => {
  router.push({ name: 'Login' })
}
</script>

<style scoped>
.signup-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(135deg, #ff5f6d, #ffc371);
  font-family: 'Arial', sans-serif;
}

.signup-card {
  background-color: #fff;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
  max-width: 400px;
  width: 100%;
  text-align: center;
}

.signup-title {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #333;
}

.signup-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
  color: #555;
}

.form-input {
  padding: 0.8rem;
  border-radius: 10px;
  border: 1px solid #ddd;
  width: 100%;
  font-size: 1rem;
}

.form-input:focus {
  outline: none;
  border-color: #ff5f6d;
  box-shadow: 0 0 8px rgba(255, 95, 109, 0.2);
}

.signup-button {
  background-color: #ff5f6d;
  color: white;
  padding: 0.8rem;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  font-size: 1.1rem;
  transition: background-color 0.3s ease;
}

.signup-button:hover {
  background-color: #e14a55;
}

.login-redirect {
  margin-top: 1rem;
  color: #555;
}

.login-link {
  color: #ff5f6d;
  font-weight: bold;
  cursor: pointer;
  text-decoration: none;
}

.login-link:hover {
  text-decoration: underline;
}
</style>
