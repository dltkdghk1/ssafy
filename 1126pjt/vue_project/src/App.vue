<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
/* 전역 CSS */
html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
  overflow: auto; /* 스크롤 가능하도록 설정 */
  box-sizing: border-box;
  background-color: #e0e0e0; /* 전체 배경을 회색으로 설정 */
}

#app {
  height: 100%;
  width: 100%;
  overflow: auto; /* 페이지 전체 스크롤 가능 */
}

.homepage-container {
  display: flex;
  height: 100%;
  width: 100%;
  overflow: auto; /* 페이지 전체를 스크롤 가능하도록 설정 */
  font-family: 'Arial', sans-serif;
  box-sizing: border-box;
}
</style>
