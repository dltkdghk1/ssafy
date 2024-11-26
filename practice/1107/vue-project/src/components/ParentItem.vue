<template>
    <p>{{ myProp.id }}</p>
    <p>{{ myProp.name }}</p>
</template>

<script setup>
    // 내려받은 props 정의 - defineProps
    defineProps({
        myProp: Object
    })
</script>

<style scoped>

</style>