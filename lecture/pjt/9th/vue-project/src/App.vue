<template>
  <div>
    <AppNavbar />
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AppNavbar from '@/components/Common/AppNavbar.vue';
</script>

<style scoped>

</style>
