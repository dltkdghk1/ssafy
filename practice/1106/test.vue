<!-- html코드 -->
<template>
    <div class="greeting">
        {{ msg }}
    </div>
</template>

<!-- js코드 -->
<script setup>
// const {ref} = Vue
import {ref} from 'vue'

const msg = ref('Hello World!')


// return {msg}
// app.mount(.greeting)
// 둘다 할 필요가 없어짐
</script>

<!-- CSS코드 -->
 <!-- scoped 이 파일에서 작성하는 style은 이 파일의 template에만 적용된다. -->
<style scoped>
.greeting {
    color: crimson;
}
</style>