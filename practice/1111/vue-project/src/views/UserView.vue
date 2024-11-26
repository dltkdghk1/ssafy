<template>
    <div>
        <RouterLink :to="{name: 'user-profile'}">Profile</RouterLink>
        <RouterLink :to="{name: 'user-posts'}">Posts</RouterLink>
        
        <h1>User View</h1>
        <h2>{{ userId }}번 user 페이지</h2>

        <button @click="goHome">홈으로</button>

        <button @click="routeUpdate">100번 유저의 페이지</button>
        <!-- 중첩라우트의 컴포넌트가 렌더링 -->
        <RouterView />
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView, useRoute, useRouter } from 'vue-router';
// leave: 페이지 떠날 떄
// update: 수정할 때
import { onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router';

const route = useRoute()

const router = useRouter()

const userId = ref(route.params.id)

const goHome = function () {
    // router.push() : 이전페이지로 돌아갈 수 있음 (히스토리 추가) (a -> b -> c에서 이전페이지로 가면 b)
    // router.replace() : 이전페이지로 돌아갈 수 없음 (히스토리에 추가 안됨) (a -> b -> c에서 뒤로 가면 a)
    router.replace({ name: 'home' })
}

const routeUpdate = function () {
    router.push({ name: 'user', params: { id: 100 } })
} 

onBeforeRouteLeave((to, from) => {
    // confirm 사용자에게 묻기
    const answer = window.confirm('정말 떠나실 건가요 ?')
    if (answer === false) {
        return false // 아니요 -> 페이지 이동 false
    }
})

// from : 1번, to 100번
onBeforeRouteUpdate((to, from) => {
    userId.value = to.params.id
})

</script>

<style scoped>

</style>