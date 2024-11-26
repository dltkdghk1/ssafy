<template>
  <div>
    <h1>상품 목록 리스트</h1>
    <div class="product-list">
      <div 
        v-for="product in store.products"
        :key="product.id"
        class="product-card"
      >
        <img :src="product.image" alt="" class="product-img">
        <div class="product-detail">
          <h3>{{ product.title }}</h3>
          <p>가격: ${{ product.price }}</p>
          <button @click="goDetail(product)">상세페이지</button>
          <button @click="addToCart(product)">장바구니</button>
        </div>
      </div>
    </div>
    {{ store.products }}
  </div>
</template>

<script setup>
import { usecartStore } from '@/stores/cart';
import { onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const store = usecartStore()
const router = useRouter()

// API로 데이터를 다운로드 받아야한다.
// DOM입장에서 없는 데이터로 화면을 그리려고 시도할 수 있ㄷ.
// -> 데이터 다운로드는 DOM이 그려지고 난 후에 가져오는 것을 권장
onMounted(() => {
  store.getProducts()
})

const goDetail = function (product) {
  router.push(`/${product.id}`)
}

const addToCart = (product) => {
  store.addToCart(product)
  router.push('/cart')
}
</script>

<style scoped>
.product-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.product-card {
  border: 1px solid #000;
  width: 200px;
  padding: 15px;
}

.product-img {
  width: 100%;
}


.product-detail {
  text-align: center;
}
</style>