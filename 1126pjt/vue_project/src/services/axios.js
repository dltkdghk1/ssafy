import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000',  // Django 백엔드 서버 주소로 변경
});

instance.interceptors.request.use((config) => {
  const token = localStorage.getItem('authToken');
  const csrfToken = document.cookie.split('; ').find(row => row.startsWith('csrftoken')).split('=')[1]; // CSRF 토큰 가져오기
  if (token) {
    config.headers.Authorization = `Token ${token}`;
  }
  if (csrfToken) {
    config.headers['X-CSRFToken'] = csrfToken;
  }
  return config;
}, (error) => {
  return Promise.reject(error);
});

export default instance;
