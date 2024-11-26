<template>
    <div>
        <p>{{ myProps.id }}</p>
        <p>{{ myProps.name }}</p>
    </div>
</template>

<script setup>
defineProps({
    myProps: Object
})
</script>

<style scoped>

</style>