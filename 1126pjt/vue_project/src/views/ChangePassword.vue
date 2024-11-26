<template>
  <div class="password-change-container">
    <div class="password-change-card">
      <h2 class="password-change-title">비밀번호 변경</h2>
      <form @submit.prevent="djangoSignUp" class="password-change-form">
        <div class="form-group">
          <label for="password1" class="form-label">비밀번호:</label>
          <input type="password" id="password1" v-model.trim="password1" class="form-input" placeholder="Enter new password" required>
        </div>
        <div class="form-group">
          <label for="password2" class="form-label">비밀번호 확인:</label>
          <input type="password" id="password2" v-model.trim="password2" class="form-input" placeholder="Confirm new password" required>
        </div>
        <button type="submit" class="password-change-button">변경</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from '../services/axios';
import { useRouter } from 'vue-router';

const router = useRouter();
const password1 = ref(null);
const password2 = ref(null);

const djangoSignUp = async function () {
  try {
    const response = await axios.post('http://127.0.0.1:8000/auth/password/change/', {
      new_password1: password1.value,
      new_password2: password2.value,
    });
    alert('비밀번호가 변경됐습니다.');
    router.push({ name: 'user' });
  } catch (error) {
    console.error(error);
    alert('비밀번호 변경 중 오류가 발생했습니다. 다시 시도해주세요.');
  }
};
</script>

<style scoped>
.password-change-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(135deg, #ff5f6d, #ffc371);
  font-family: 'Arial', sans-serif;
}

.password-change-card {
  background-color: #fff;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
  max-width: 400px;
  width: 100%;
  text-align: center;
}

.password-change-title {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #333;
}

.password-change-form {
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

.password-change-button {
  background-color: #ff5f6d;
  color: white;
  padding: 0.8rem;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  font-size: 1.1rem;
  transition: background-color 0.3s ease;
}

.password-change-button:hover {
  background-color: #e14a55;
}
</style>
