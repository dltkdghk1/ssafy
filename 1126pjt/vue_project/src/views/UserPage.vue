<template>
  <div class="profile-container">
    <!-- Header Section -->
    <div class="profile-header">
      <div class="user-info">
        <img :src="`https://i.pravatar.cc/150?u=${user.username}`" alt="Profile Picture" class="profile-pic">
        <h2>{{ user.username }}의 프로필</h2>
      </div>
      <div class="profile-buttons">
        <button @click="goToHome" class="profile-button home-button">🏠 홈으로</button>
        <button @click="goToPassword" class="profile-button password-button">🔒 비밀번호 변경</button>
      </div>
    </div>

    <!-- Watch History Section -->
    <h2 class="record">시청 기록</h2>
    <div class="history-container">
      <div v-for="movie in history" :key="movie.movie.id" class="history-card">
        <img :src="`https://image.tmdb.org/t/p/w200/${movie.movie.poster_path}`" alt="Movie Poster" class="movie-poster">
        <div class="history-details">
          <p class="movie-title">🎬 제목: {{ movie.movie.title }}</p>
          <p class="watch-percentage">📊 시청 비율: {{ formatPercentage(movie.watched_percentage) }}%</p>
        </div>
      </div>
    </div>

    <!-- My Articles Section -->
    <h2 class="article">작성한 게시물</h2>
    <div class="article-container">
      <div v-for="article in myArticle" :key="article.id" class="article-card">
        <h3>{{ article.title }}</h3>
        <p>{{ article.content }}</p>
        <button @click="goToArticle(article.id)" class="view-article-button">게시물 보기</button>
      </div>
    </div>

    <!-- My Comments Section -->
    <h2 class="comment">작성한 댓글</h2>
    <div class="comments-container">
      <div v-for="comment in myComment" :key="comment.id" class="comment-card">
        <img :src="`https://image.tmdb.org/t/p/w200/${comment.movie.poster_path}`" alt="Movie Poster" class="comment-movie-poster">
        <div class="comment-details">
          <p class="movie-title">🎬 영화 제목: {{ comment.movie.title }}</p>
          <p class="comment-content">💬 댓글: "{{ comment.content }}"</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from '../services/axios';
import router from '../router';

const user = ref({});
const history = ref([]);
const myArticle = ref([]);
const myComment = ref([]);

// 시청 기록 가져오기
const fetchWatchHistory = async () => {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/v1/accounts/watch-history/`);
    const rawData = response.data;

    // 중복 제거 및 watched_percentage 높은 순으로 정렬
    const uniqueMovies = {};
    rawData.forEach((item) => {
      const movieId = item.movie.id;
      if (
        !uniqueMovies[movieId] ||
        item.watched_percentage > uniqueMovies[movieId].watched_percentage
      ) {
        uniqueMovies[movieId] = item;
      }
    });

    history.value = Object.values(uniqueMovies).sort(
      (a, b) => b.watched_percentage - a.watched_percentage
    );
  } catch (error) {
    console.error('시청 기록을 가져오는 중 오류 발생:', error);
  }
};

// 작성한 게시물 가져오기
const fetchMyArticles = async () => {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/v1/myarticle/`);
    myArticle.value = response.data;
  } catch (error) {
    console.error('게시물을 가져오는 중 오류 발생:', error);
  }
};

// 작성한 댓글 가져오기
const fetchMyComment = async () => {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/api/v1/movies/mycomment/`);
    myComment.value = response.data;
  } catch (error) {
    console.error('댓글을 가져오는 중 오류 발생:', error);
  }
};

// 유저 정보 가져오기
const fetchUser = async () => {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/auth/user/`);
    user.value = response.data;
  } catch (error) {
    console.error('유저 정보를 가져오는 중 오류 발생:', error);
  }
};

// 실시간 업데이트
const setupRealTimeUpdates = () => {
  setInterval(() => {
    fetchWatchHistory();
    fetchMyArticles();
    fetchMyComment();
  }, 10000); // 10초마다 데이터 업데이트
};

// 날짜 포맷팅 함수
const formatDate = (dateString) => {
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(dateString).toLocaleDateString(undefined, options);
};

const formatPercentage = (percentage) => {
  return percentage.toFixed(1); // 소수점 첫째 자리까지 표시
};

onMounted(() => {
  fetchUser();
  fetchWatchHistory();
  fetchMyArticles();
  fetchMyComment();
  setupRealTimeUpdates();
});

const goToPassword = () => {
  router.push({ name: 'password' });
};

const goToHome = () => {
  router.push({ name: 'ShortsPage' });
};

const goToArticle = (articleId) => {
  router.push({ name: 'detail', params: { id: articleId } });
};
</script>

<style scoped>

.record {
  margin: 40px;
}

.article {
  margin: 40px;
}

.comment {
  margin: 40px;
}

/* Profile Header */
.profile-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 5px;
  background: linear-gradient(45deg, #ff5f6d, #ffc371);
  border-radius: 10px;
  margin-bottom: 20px;
}

.user-info {
  display: flex;
  align-items: center;
}

.profile-pic {
  border-radius: 50%;
  width: 45px;
  height: 45px;
  margin-right: 7px;
}

.profile-buttons {
  display: flex;
  gap: 10px;
}

.profile-button {
  padding: 10px 20px;
  font-size: 1rem;
  background-color: #fff;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.profile-button:hover {
  background-color: #e14a55;
  transform: scale(1.05);
}

/* History Container */
.history-container {
  display: flex;
  flex-wrap: wrap;
  gap: 50px;
  margin-top: 20px;
  margin-left: 70px;
  margin-bottom: 100px;
}

.history-card {
  width: 200px;
  height: 400px;
  border-radius: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  transition: transform 0.3s ease;
}

.history-card:hover {
  transform: translateY(-5px);
}

.movie-poster {
  width: 100%; /* 부모 요소 너비와 동일 */
  height: 70%; /* 부모 요소 높이의 90% */
  object-fit: cover; /* 이미지가 잘리더라도 카드 크기에 맞춤 */
}

.history-details {
  font-size: 0.85rem; /* 글자 크기 설정 */
  font-weight: bold; /* 굵게 설정 */
  text-align: center; /* 텍스트 가운데 정렬 */
  margin: 0 auto; /* 요소 자체도 가운데로 이동 */
  max-width: 90%; /* 부모 요소의 가로폭을 넘지 않도록 설정 */
  overflow: hidden; /* 넘치는 텍스트 숨김 */
  display: -webkit-box; /* Flexbox처럼 작동하는 웹킷 박스를 사용 */
  -webkit-line-clamp: 2; /* 최대 2줄까지만 표시 */
  -webkit-box-orient: vertical; /* 박스 방향을 수직으로 설정 */
  line-height: 1.6rem; /* 줄 간격 설정 */
  word-wrap: break-word; /* 긴 단어가 있으면 자동으로 줄바꿈 */
  word-break: keep-all; /* 단어가 잘리지 않도록 설정 */
  padding: 15px;
}

.movie-title {
  font-size: 0.85rem; /* 글자 크기 설정 */
  font-weight: bold; /* 굵게 설정 */
  text-align: center; /* 텍스트 가운데 정렬 */
  margin: 0 auto; /* 요소 자체도 가운데로 이동 */
  max-width: 90%; /* 부모 요소의 가로폭을 넘지 않도록 설정 */
  overflow: hidden; /* 넘치는 텍스트 숨김 */
  display: -webkit-box; /* Flexbox처럼 작동하는 웹킷 박스를 사용 */
  -webkit-line-clamp: 2; /* 최대 2줄까지만 표시 */
  -webkit-box-orient: vertical; /* 박스 방향을 수직으로 설정 */
  line-height: 1.6rem; /* 줄 간격 설정 */
  word-wrap: break-word; /* 긴 단어가 있으면 자동으로 줄바꿈 */
  word-break: keep-all; /* 단어가 잘리지 않도록 설정 */
}


.watch-percentage {
  color: black;
}

/* Articles Container */
.article-container {
  display: flex;
  flex-wrap: wrap;
  gap: 50px;
  margin-top: 20px;
  margin-left: 70px;
  margin-bottom: 100px;
}

.article-card {
  width: 200px;
  height: 250px;
  border-radius: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  transition: transform 0.3s ease;
  display: flex; /* 콘텐츠를 가운데 정렬하기 위해 추가 */
  flex-direction: column; /* 수직 방향으로 정렬 */
  align-items: center; /* 수평 가운데 정렬 */
  justify-content: space-between; /* 수직 간격을 적절히 배치 */
  padding: 15px; /* 내부 여백 추가 */
  text-align: center; /* 텍스트 가운데 정렬 */
}

.view-article-button {
  margin-top: 10px;
  padding: 10px 20px;
  background-color: #e14a55;
  color: white;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.view-article-button:hover {
  background-color: #e14a55;
}

/* Comments Container */
.comments-container {
  display: flex;
  flex-wrap: wrap;
  gap: 50px;
  margin-top: 20px;
  margin-left: 70px;
  margin-bottom: 100px;
}

.comment-card {
  width: 200px;
  height: 400px;
  border-radius: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  transition: transform 0.3s ease;
}

.comment-card:hover {
  transform: translateY(-5px);
}

.comment-movie-poster {
  width: 100%;
  height: 300px;
  object-fit: cover;
}

.comment-details {
  padding: 10px;
}

.comment-content {
  font-size: 0.85rem; /* 글자 크기 설정 */
  font-weight: bold; /* 굵게 설정 */
  text-align: center; /* 텍스트 가운데 정렬 */
  margin: 0 auto; /* 요소 자체도 가운데로 이동 */
  max-width: 90%; /* 부모 요소의 가로폭을 넘지 않도록 설정 */
  overflow: hidden; /* 넘치는 텍스트 숨김 */
  display: -webkit-box; /* Flexbox처럼 작동하는 웹킷 박스를 사용 */
  -webkit-line-clamp: 2; /* 최대 2줄까지만 표시 */
  -webkit-box-orient: vertical; /* 박스 방향을 수직으로 설정 */
  line-height: 1.6rem; /* 줄 간격 설정 */
  word-wrap: break-word; /* 긴 단어가 있으면 자동으로 줄바꿈 */
  word-break: keep-all; /* 단어가 잘리지 않도록 설정 */
}

.comment-date {
  color: #777;
  font-size: 0.9rem;
}
</style>
