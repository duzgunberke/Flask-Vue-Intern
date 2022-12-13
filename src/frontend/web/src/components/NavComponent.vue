<template>
        <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
    <div class="container-fluid">
      <router-link class="navbar-brand" to="/" >Blog</router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav me-auto mb-2 mb-md-0" v-if="!user">
          <li class="nav-item">
            <router-link class="nav-link" to="/login">Login</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/register">Sign Up</router-link>
          </li>
        </ul>
        <ul class="navbar-nav me-auto mb-2 mb-md-0" v-if="user">
          <li class="nav-item">
            <a href="javascript:void(0)" @click="handleClick" class="nav-link">Logout</a>
          </li>
          <li class="nav-item">
            <router-link  class="nav-link" to="/mypage">My Blogs</router-link>
          </li>
        </ul>
        <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>
</template>

<script>
import {mapGetters} from 'vuex'
export default{
    name:'NavComponent',
    
    methods:{
      handleClick(){
        window.localStorage.removeItem('token');
        window.localStorage.removeItem('user',null);
        this.$store.dispatch('user',null);
        this.$router.push('/');
    
      }
    },
    computed:{
      ...mapGetters(['user'])
    }
}
</script>