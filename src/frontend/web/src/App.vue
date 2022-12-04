<template>
  <div id="app">
    <NavComponent :user="user"/> 
    <div class="auth-wrapper">
      <div class="auth-inner">
         <RouterView :user="user"/>
      </div>
    </div>
  </div>
</template>

<script>
import NavComponent from './components/NavComponent.vue'
// import axios from 'axios';

export default{
  name: 'App',
  components:{
    NavComponent,
  },
  data(){
        return {
            user:null
        }
    },
     created(){
        // const response= axios.get('currentuser',{
        //     headers:{
        //         Authorization:'Bearer '+ localStorage.getItem('token')
        //     }
        // });
        // console.log(response);
        this.user=JSON.parse(window.localStorage.getItem('user'));
        console.log("AAAAAAAAA")
        console.log(this.user)
        
        
    }
}

</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100;200;300;500&family=Open+Sans:wght@400;600;700&display=swap" rel="stylesheet');
*{
  box-sizing: border-box;
}

body{
  background-color:#FBFACD!important;
  min-height:100vh;
  font-weight: 400;
  font-family: 'Fira Sans',sans-serif;
}

h1,h2,h3,h4,h5,h6,label,span{
  font-weight:500;
  font-family:Fira Sans,sans-serif;
}

body,html,#app,#root,auth-wrapper{
  width:100%;
  height:100%;
}

#app{
  text-align: center;
}

.auth-inner{
  width:450px;
  margin:auto;
  background:#ffffff;
  padding:40px 55px 45px 55px;
  border-radius:15px;
  transition:all .3s;
}

.auth-wrapper{
  margin-top: 200px;
  display:flex;
  justify-content:center;
  flex-direction: column;
  text-align: left;
}

.auth-wrapper .form-control:focus{
  border-color: blue;
  box-shadow:none;
}



.custom-control-label{
  font-weight:400;
}
</style>
