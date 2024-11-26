<template>
  <div>
    <h1>상세 페이지</h1>
    <div v-if="product">
      <img :src="product.image" alt="" width="200px">
      <h3>{{ product.title }}</h3>
      <p>가격: {{ product.price }}</p>
      <p>카테고리: {{ product.cartegory }}</p>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { usecartStore } from '@/stores/cart';

const store = usecartStore()
const route = useRoute()
const productId = route.params.product_id

const product = store.getProductById(productId)
</script>

<style scoped>

</style>