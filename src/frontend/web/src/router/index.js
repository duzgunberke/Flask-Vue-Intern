import HomeComponent from '../components/HomeComponent.vue'
import LoginComponent from '../components/LoginComponent.vue'
import RegisterComponent from '../components/RegisterComponent.vue'
import BlogListComponent from '../components/BlogListComponent.vue'
import AddOrUpdateBlog from '../components/AddOrUpdateBlog.vue'


import { createRouter, createWebHistory } from "vue-router"
    const routeInfos = [
        {
            path : "/",
            component : BlogListComponent
        },
        {
            path : "/mypage",
            component : HomeComponent
        },
        {
            path : "/login",
            component : LoginComponent
        },
        {
            path : "/register",
            component : RegisterComponent
        },
        {
            path : "/addorupdateblog",
            component : AddOrUpdateBlog
        }
    ]
    
    const router = createRouter({
        history : createWebHistory(),
        routes : routeInfos
    })
    
    export default router;