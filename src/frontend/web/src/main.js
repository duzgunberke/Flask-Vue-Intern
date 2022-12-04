import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index.js'
import './conf/axios.js'
//import store from './store/vuex'

const app = createApp(App)

app.use(router);
//app.use(store);

app.mount('#app')



