<!-- props : 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달하는 방법 -->
<template>
  <!-- "message"를 자식에게 전달하는 정적 props -->
  <!-- name변수를 자식에게 전달하는 동적 props -->
  <!-- my-msg : 케밥 케이스 (HTML 속성) -->
  <ParentChild
    @some-event="someCallback"
    @emit-args="getNumbers"
    @update-name="updateName"
    my-msg="message"
    :dynamic-props="name"
  />
  <ParentItem v-for="item in items" :key="item.id" :my-prop="item" />
</template>

<script setup>
import { ref } from "vue";
import ParentChild from "@/components/ParentChild.vue";
import ParentItem from "@/components/ParentItem.vue";

const name = ref("Bob");
const items = ref([
  { id: 1, name: "사과" },
  { id: 2, name: "바나나" },
  { id: 3, name: "딸기" },
]);

const someCallback = function () {
  alert("ParentChild가 발신한 이벤트를 수신");
};

const getNumbers = function (...args) {
  alert(`ParentChild가 발신한 추가인자 ${args}`);
};

const updateName = function () {
  name.value = 'Bella'
};
</script>

<style scoped></style>
