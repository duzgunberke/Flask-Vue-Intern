import HomeComponent from '../components/HomeComponent.vue'
import LoginComponent from '../components/LoginComponent.vue'
import RegisterComponent from '../components/RegisterComponent.vue'
import BlogListComponent from '../components/BlogListComponent.vue'
import AddBlog from '../components/AddBlog.vue'
import BlogDetail from '../components/BlogDetail.vue'
import UpdateBlog from '../components/UpdateBlog.vue'

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
            path : "/blogdetail/:id",
            component : BlogDetail
        },
        {
            path : "/addblog",
            component : AddBlog
        },
        {
            path : "/updateblog/:id",
            component : UpdateBlog
        }
    ]
    
    const router = createRouter({
        history : createWebHistory(),
        routes : routeInfos
    })
    
    export default router;