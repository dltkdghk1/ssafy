import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

import axios from 'axios'
export const useCounterStore = defineStore('counter', () => {

  const articles = ref([])
  const API_URL = "http://127.0.0.1:8000"

  // 프론트에서 백엔드로 요청 보내면 DRF로 응답을 받는다
  // 그 응답을 저장해야한다!! articles 배열에 저장하는 함수
  const getArticles = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`
    })
      .then(res =>{
        articles.value = res.data
      })
      .catch(err => console.log(err))
  }
  return { articles, API_URL, getArticles }
}, { persist: true })
