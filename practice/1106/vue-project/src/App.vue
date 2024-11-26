<!-- Django -->
<!-- 1. pip : python install package -->
<!-- 2. venv(가상환경) - 버전과리(버전충돌방지) -->
<!--                   - requirements.txt 의존성 파일관리 -->
<!-- 3. 패키지 설치 :  -->

<!-- vue -->
<!-- 1. npm package manager(파이썬의 pip와 같다) -->
<!-- 2. 프로젝트의 의존성 관리 : package.json -->
<!-- 프로젝트별 필요한 패키지 저장소 역할 : node_modules -->
<!-- vue는 package.json, node_modules로 환경을 관리 -> venv가 필요없다. -->

<template>
  <h1>App.vue</h1>
  <!-- 자식 컴포넌트 -->
  <!-- selg-closing 태그 -->
  <MyComponent />
</template>

<script setup>
// 컴포넌트 불러오기 방법 1. 상대경로
// import MyComponent from './components/MyComponent.vue'
// 컨포넌트 불러오기 방법 2. @ 별칭 사용 (src 디렉토리 의미)
import MyComponent from '@/components/MyComponent.vue';
// assets과 components의 차이
// 동적으로 변경될 수 있는 데이터(.vue)와 로직 -> components
// 정적 리소스 파일들 -> assets (.jpg, .png, .css, .json, .ttf ....)

</script>

<style scoped>

</style>