import App from './App.vue'
import router from './router/index.js'
import './conf/axios.js'
import store from './store/vuex'

import { createApp } from "vue";

const app = createApp(App)
// Vue.use(Vuex);
app.use(store);
app.use(router);

app.mount('#app')



