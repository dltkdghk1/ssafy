import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store'; // 새로 추가한 스토어 가져오기

createApp(App).use(router).use(store).mount('#app');
