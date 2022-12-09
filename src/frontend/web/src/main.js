import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index.js'
import './conf/axios.js'
import store from './store/vuex'
// import Vue from 'vue';
// import Vuex from 'vuex';

const app = createApp(App)
// Vue.use(Vuex);
app.use(router);
app.use(store);

app.mount('#app')



