<template>
  <p>{{ myMsg }}</p>
  <button @click="updateName">이름변경</button>
</template>

<script setup>
defineProps({
  myMsg: String,
});

const emit = defineEmits(["updateName"]);

// 함수명과 emit명은 달라도 상관없다
const updateName = function () {
  emit("updateName");
};
</script>

<style scoped></style>
