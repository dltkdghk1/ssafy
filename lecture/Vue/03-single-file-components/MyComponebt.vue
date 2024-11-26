<template>
    <div class="greeting">
        {{ msg }}
    </div>
</template>

<!-- Vue CDN필요 없어짐 -->
<script setup>
import { ref } from 'vue'

const msg = ref('hello')

</script>

<style scoped>
.greeting {
    color: red;
}
</style>