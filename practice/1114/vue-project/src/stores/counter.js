// store/counter.js

import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  // state 영역
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()

  // 액션 영역
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      // 토큰
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const signUp = function (payload) {
    const { username, password1, password2 } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data:{
        username, password1, password2
      }
    })
      .then((res) => {
        console.log('회원가입에 성공했습니다')
      })
      .catch((err) => {
        console.log('회원가입에 실패했습니다')
      })
  } 

  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res)=> {
        token.value = res.data.key
        router.push({ name: 'ArticleView' })
        console.log('로그인 되었습니다.')
      })
      .catch((err)=> {
        console.log(err)
      })
  }

  // getter 영역
  // 로그인 영역 계산
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  return { articles, API_URL, getArticles ,signUp, logIn, token, isLogin }
}, { persist: true })