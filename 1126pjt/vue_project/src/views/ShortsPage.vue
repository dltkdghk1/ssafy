<template>
  <div class="homepage-container">
    <div class="sidebar">
      <div class="sidebar-logo">
        MovieClip
      </div>
      <nav class="nav-icons">
        <button @click="goToCommunity" class="icon-button community-icon">
          <i class="fas fa-comments"></i>
          <span>Community</span>
        </button>
        <button @click="goToMyPage" class="icon-button user-icon">
          <i class="fas fa-user"></i>
          <span>My Page</span>
        </button>
        <button v-if="!isAuthenticated" @click="goToLoginPage" class="icon-button login-icon">
          <i class="fas fa-sign-in-alt"></i>
          <span>Login</span>
        </button>
        <button v-else @click="handleLogout" class="icon-button logout-icon">
          <i class="fas fa-sign-out-alt"></i>
          <span>Logout</span>
        </button>
      </nav>
    </div>

    <div class="main-content">
      <div class="video-feed">
        <div v-if="movies.length > 0">
          <div class="video-container">
            <TrailerPlayer v-if="movies[currentIndex].video_id" :videoId="movies[currentIndex].video_id" />
            <p v-else class="loading-trailer">Loading trailer...</p>
            <button class="toggle-comments-button" @click="toggleComments">
              {{ commentsVisible ? '💬' : '💬' }}
            </button>
            
          </div>
        </div>
        <div v-else>
          <p class="loading">Loading movies...</p>
        </div>
        
      </div>

      <div class="info-section" v-if="movies.length > 0">
        <div class="movie-info">
          <h3>{{ movies[currentIndex].title }}</h3>
          <p><strong>Release Date:</strong> {{ movies[currentIndex].release_date }}</p>
          <p><strong>Rating:</strong> {{ movies[currentIndex].vote_average }} / 10</p>
          <p class="movie_content"><strong>Summary:</strong> {{ movies[currentIndex].content }}</p>
        </div>
      </div>

      <div class="comments-section" :class="{ visible: commentsVisible }">
        <div v-if="commentsVisible" class="comments-container">
          <h2>댓글 {{ comments.number_of_comments }}</h2>
          
          <div class="comments-list">
            <div v-for="comment in comments.comment_set" :key="comment.id" class="comment">
              <p><strong>{{ comment.user.username }}:</strong> {{ comment.content }}</p>
              <button @click="deleteComment(comment.id)" class="delete-comment-button">삭제</button>
            </div>
          </div>

          <form @submit.prevent="addComment" class="add-comment-form">
            <textarea v-model="newComment" placeholder="댓글 추가..." class="comment-input"></textarea>
            <button type="submit" class="add-comment-button">등록</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>



<script>
import { ref, onMounted, computed, watch, onBeforeUnmount } from 'vue';
import axios from '../services/axios';
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';
import TrailerPlayer from '../components/TrailerPlayer.vue';

export default {
  name: 'ShortsPage',
  components: {
    TrailerPlayer,
  },
  setup() {
    const store = useStore();
    const router = useRouter();
    const isAuthenticated = computed(() => store.getters.isAuthenticated);
    const movies = ref([]);
    const currentIndex = ref(0);
    const commentsVisible = ref(false);
    const comments = ref([]);
    const newComment = ref('');
    const startTime = ref(null);
    const watchTime = ref(0);

    onMounted(() => {
      if (!store.state.token) {
        console.error('토큰이 없습니다. 로그인을 먼저 해주세요.');
        router.push({ name: 'Login' });
        return;
      }

      // 영화 데이터 가져오기
      axios.get('http://127.0.0.1:8000/api/v1/movies/')
        .then((response) => {
          if (response.status === 200) {
            movies.value = response.data;
            loadComments(); // 첫 번째 비디오의 댓글 불러오기
            startWatch(); // 영화 시청 시간 시작
          } else {
            console.error('영화 목록을 가져오는 데 실패했습니다.');
          }
        })
        .catch((error) => {
          console.error('영화 목록을 가져오는 중 오류 발생:', error);
        });

      // Wheel 이벤트 등록
      window.addEventListener('wheel', handleScroll, { passive: false });
    });

    onBeforeUnmount(() => {
      recordWatchTime();
      // Wheel 이벤트 제거
      window.removeEventListener('wheel', handleScroll);
    });

    const startWatch = () => {
      startTime.value = new Date().getTime();
    };

    const recordWatchTime = async () => {
      if (startTime.value !== null) {
        const endTime = new Date().getTime();
        watchTime.value += (endTime - startTime.value) / 1000;

        let watchedPercentage = (watchTime.value / (movies.value[currentIndex.value]?.duration || 120)) * 100;
        watchedPercentage = Math.min(watchedPercentage, 100);

        try {
          if (!store.state.token) {
            console.error('토큰이 없습니다. 로그인을 먼저 해주세요.');
            return;
          }

          const response = await axios.post('/api/v1/accounts/watch-history/', {
            movie_id: movies.value[currentIndex.value]?.id,
            watched_percentage: watchedPercentage,
          });

          if (response.status === 201) {
            console.log('Watch history recorded:', watchedPercentage);
          } else {
            console.error('Watch history 기록 실패:', response.data);
          }
        } catch (error) {
          console.error('Failed to record watch history:', error);
        }
      }
      watchTime.value = 0;
    };

    watch(currentIndex, (newIndex, oldIndex) => {
      if (oldIndex !== newIndex) {
        recordWatchTime();
        startWatch();
        loadComments(); // 인덱스 변경 시 새로운 댓글 데이터 로드
      }
    });

    const handleScroll = (event) => {
      event.stopPropagation(); // 페이지 전체 스크롤 방지
      if (event.deltaY > 0) {
        nextTrailer();
      } else if (event.deltaY < 0) {
        previousTrailer();
      }
    };

    const nextTrailer = () => {
      if (currentIndex.value < movies.value.length - 1) {
        currentIndex.value++;
      }
    };

    const previousTrailer = () => {
      if (currentIndex.value > 0) {
        currentIndex.value--;
      }
    };

    const goToLoginPage = () => {
      router.push({ name: 'Login' });
    };

    const handleLogout = () => {
      store.dispatch('logout');
      router.push({ name: 'ShortsPage' });
    };

    const goToCommunity = () => {
      router.push({ name: 'community' });
    };

    const goToMyPage = () => {
      router.push({ name: 'user' });
    };

    const toggleComments = () => {
      commentsVisible.value = !commentsVisible.value;
      if (commentsVisible.value) {
        loadComments();
      }
    };

    const loadComments = () => {
      const movieId = movies.value[currentIndex.value].id;
      if (!movieId) return;

      axios.get(`http://127.0.0.1:8000/api/v1/movies/${movieId}/`)
        .then((response) => {
          if (response.status === 200) {
            comments.value = response.data;
          } else {
            console.error('댓글을 가져오는 데 실패했습니다.');
          }
        })
        .catch((error) => {
          console.error('댓글을 가져오는 중 오류 발생:', error);
        });
    };

    const addComment = () => {
      const movieId = movies.value[currentIndex.value]?.id;
      if (!movieId || !newComment.value.trim()) return;

      axios.post(`http://127.0.0.1:8000/api/v1/movies/${movieId}/comments/`, {
        content: newComment.value,
      })
        .then((response) => {
          if (response.status === 201) {
            if (!Array.isArray(comments.value)) {
              comments.value = [];
            }
            comments.value.push(response.data);
            newComment.value = '';
            loadComments(); // 댓글 추가 후 새로고침
          } else {
            console.error('댓글 작성 실패:', response.data);
          }
        })
        .catch((error) => {
          console.error('댓글 작성 중 오류 발생:', error);
        });
    };

    const deleteComment = (commentId) => {
      axios.delete(`http://127.0.0.1:8000/api/v1/movies/comments/${commentId}/`)
        .then((response) => {
          if (response.status === 204) {
            if (!Array.isArray(comments.value)) {
              comments.value = [];
            }
            comments.value = comments.value.filter(comment => comment.id !== commentId);
            loadComments(); // 댓글 삭제 후 새로고침
          } else {
            console.error('댓글 삭제 실패:', response.data);
          }
        })
        .catch((error) => {
          console.error('댓글 삭제 중 오류 발생:', error);
        });
    };

    return {
      movies,
      currentIndex,
      handleScroll,
      goToLoginPage,
      handleLogout,
      isAuthenticated,
      goToCommunity,
      goToMyPage,
      commentsVisible,
      toggleComments,
      comments,
      newComment,
      addComment,
      deleteComment,
      nextTrailer,
      previousTrailer,
    };
  },
};
</script>

<style scoped>
.loading-trailer {
  color: white;
}

.loading {
  color: white;
}
/* 전체 페이지 스타일 */
html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
  overflow: hidden; /* 가로 스크롤 방지 */
  box-sizing: border-box;
}

.homepage-container {
  display: flex;
  height: 100%;
  width: 100%;
  overflow: auto;
  font-family: 'Arial', sans-serif;
  box-sizing: border-box;
}

/* 사이드바 스타일 */
.sidebar {
  width: 150px;
  background-color: #ff5f6d;
  color: #fff;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 30px 0;
  box-shadow: 2px 0 10px rgba(0, 0, 0, 0.2);
  position: fixed;
  left: 0;
  top: 0;
  height: 100%;
  z-index: 10; /* 다른 요소보다 위에 배치 */
}

/* MovieClip 로고 스타일 */
.sidebar-logo {
  font-size: 1.7rem; /* 큰 글자 크기 */
  font-weight: bold; /* 굵은 글씨 */
  color: #fff;
  text-align: center;
}

.nav-icons {
  display: flex;
  flex-direction: column;
  gap: 30px;
  margin-top: 50px;
}

.icon-button {
  background: none;
  border: none;
  color: #fff;
  cursor: pointer;
  transition: color 0.3s, transform 0.2s, background 0.3s;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-size: 1rem;
  padding: 10px;
  border-radius: 10px;
}

.icon-button:hover {
  color: #ff5f6d;
  transform: scale(1.15);
  background: rgba(255, 95, 109, 0.2);
}

.icon-button i {
  font-size: 2rem;
  margin-bottom: 5px;
}

/* 메인 콘텐츠 스타일 */
.main-content {
  flex-grow: 1;
  margin-left: 150px; /* 사이드바 공간 확보 */
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  text-align: center;
  overflow: hidden;
  width: calc(100% - 150px); /* 사이드바 제외한 나머지 공간을 차지하도록 설정 */
  box-sizing: border-box;
  background: #f7f7f7;
}

/* 비디오 피드 스타일 */
.video-feed {
  flex: 3;
  max-width: 600px;
  padding: 15px;
  position: relative;
  background: black;
  border-radius: 15px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
}

.video-container {
  width: 600px;
  height: 300px;
}

/* 댓글 숨김/표시 버튼 */
.toggle-comments-button {
  position: absolute;
  right: 20px;
  top: 10px;
  background: #ff5f6d;
  color: white;
  border: none;
  border-radius: 15px;
  cursor: pointer;
  font-size: 1rem;
  padding: 10px 15px;
  transition: background 0.3s, transform 0.2s;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.toggle-comments-button:hover {
  background: #ff3b4d;
  transform: scale(1.05);
}

/* 비디오 정보 섹션 */
.info-section {
  width: 607px; /* 고정 너비 */
  height: 323.44px; /* 고정 높이 */
  margin-top: 20px;
  text-align: left;
  background: rgba(255, 255, 255, 0.9);
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden; /* 내용이 넘칠 경우 숨김 처리 */
}

.info-section p {
  display: -webkit-box;
  -webkit-line-clamp: 7; /* 최대 3줄까지만 표시 */
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis; /* 넘치는 텍스트를 ...으로 표시 */
  white-space: normal; /* 줄바꿈 가능하도록 설정 */
  word-wrap: break-word; /* 단어가 너무 길 경우 자동으로 줄바꿈 */
}

/* 댓글 섹션 */
.comments-section {
  position: fixed;
  right: 0;
  top: 0;
  width: 400px;
  height: 100%;
  background: #fff;
  border-left: 2px solid #ddd;
  transition: transform 0.3s ease-in-out;
  transform: translateX(100%);
  box-shadow: -8px 0 15px rgba(0, 0, 0, 0.1);
  z-index: 5; /* 사이드바보다 뒤쪽에 위치 */
}

.comments-section.visible {
  transform: translateX(0);
}

.comments-container {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.comments-list {
  flex-grow: 1; /* 댓글 목록이 가능한 모든 공간을 차지하도록 함 */
  overflow-y: auto; /* 댓글 목록만 스크롤 가능 */
  padding: 10px;
  border-bottom: 1px solid #e0e0e0;
}

.comment {
  margin-bottom: 15px;
  padding: 5px;
  border-bottom: 1px solid #e0e0e0;
}

.add-comment-form {
  padding: 10px;
  border-top: 1px solid #e0e0e0;
  background: #ffffff; /* 배경색을 지정하여 스크롤 시 댓글 폼이 깔끔하게 보이도록 함 */
  display: flex;
  flex-direction: column;
}

.comment-input {
  width: 100%;
  height: 60px;
  margin-bottom: 10px;
  padding: 10px;
}

.add-comment-button {
  align-self: flex-end;
  padding: 10px 20px;
  font-size: 1em;
  background-color: #e14a55;
  color: white;
  border: none;
  cursor: pointer;
}

.add-comment-button:hover {
  background: #e14a55;
  transform: scale(1.05);
}

</style>