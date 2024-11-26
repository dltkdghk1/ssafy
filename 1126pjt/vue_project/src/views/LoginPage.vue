<template>
  <div class="login-container">
    <div class="login-card">
      <h2 class="login-title">로그인</h2>
      <form @submit.prevent="handleLogin" class="login-form">
        <div class="form-group">
          <label for="username" class="form-label">Username:</label>
          <input type="text" v-model="username" id="username" class="form-input" placeholder="Enter your Username" required />
        </div>
        <div class="form-group">
          <label for="password" class="form-label">Password:</label>
          <input type="password" v-model="password" id="password" class="form-input" placeholder="Enter your Password" required />
        </div>
        <button type="submit" class="login-button">Login</button>
        <button type="button" @click="goToSignupPage" class="signup-button">회원가입</button>
      </form>
      <p v-if="loginError" class="error">{{ loginError }}</p>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from '../services/axios'; // 기본 설정된 Axios 인스턴스를 가져옴
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';

export default {
  name: 'LoginPage',
  setup() {
    const store = useStore();
    const router = useRouter();
    const username = ref('');
    const password = ref('');
    const loginError = ref('');

    const goToSignupPage = function () {
      router.push({ name: 'Signup' })
    }

    const handleLogin = async () => {
      try {
        // 로그인 요청을 보낼 때 기본 설정된 axios 인스턴스 사용
        const response = await axios.post('/api/v1/accounts/custom/login/', {
          username: username.value,
          password: password.value,
        });

        // 서버 응답 처리
        if (response.data && response.data.token) {
          // Vuex Store를 통해 사용자와 토큰 정보 저장
          store.dispatch('login', { user: username.value, token: response.data.token });
          loginError.value = '';
          // 로그인 성공 시 홈 페이지로 이동
          router.push({ name: 'ShortsPage' });
        } else {
          loginError.value = 'Invalid response format';
        }
      } catch (error) {
        console.error('Login error:', error);
        // 에러 메시지를 사용자가 이해할 수 있게 개선
        if (error.response && error.response.status === 400) {
          loginError.value = 'Invalid username or password';
        } else {
          loginError.value = 'An error occurred during login. Please try again later.';
        }
      }
    };

    return {
      username,
      password,
      loginError,
      handleLogin,
      goToSignupPage
    };
  },
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(135deg, #ff5f6d, #ffc371);
  font-family: 'Arial', sans-serif;
}

.login-card {
  background-color: #fff;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
  max-width: 400px;
  width: 100%;
  text-align: center;
}

.login-title {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #333;
}

.login-form {
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

.login-button {
  background-color: #ff5f6d;
  color: white;
  padding: 0.8rem;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  font-size: 1.1rem;
  transition: background-color 0.3s ease;
}

.login-button:hover {
  background-color: #e14a55;
}

.signup-button {
  background-color: #ffc371;
  color: white;
  padding: 0.8rem;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  font-size: 1.1rem;
  transition: background-color 0.3s ease;
  margin-top: 0.5rem;
}

.signup-button:hover {
  background-color: #e0a860;
}

.error {
  color: red;
  margin-top: 1rem;
}
</style>
