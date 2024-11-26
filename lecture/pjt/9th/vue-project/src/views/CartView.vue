<template>
  <div>
    <h1>장바구니</h1>
    <div v-if="store.carts.length > 0">
      <div class="product-list">
      <div 
        v-for="product in store.carts"
        :key="product.id"
        class="product-card"
      >
        <img :src="product.image" alt="" class="product-img">
        <div class="product-detail">
          <h3>{{ product.title }}</h3>
          <p>가격: ${{ product.price }}</p>
          <button @click="goDetail(product)">상세페이지</button>
          <button @click="deleteToCart(product)">삭제</button>
        </div>
      </div>
    </div>
    </div>
    <div v-else>
      <p>장바구니가 비어 있습니다.</p>
    </div>
  </div>
</template>

<script setup>
// import router from '@/router';
import { usecartStore } from '@/stores/cart';
import { useRouter } from 'vue-router';

const router = useRouter()
const store = usecartStore()

const goDetail = function (product) {
  router.push(`/${product.id}`)
}

const deleteToCart = (product) => {
  store.deleteToCart(product.id)
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