<template>
<div>
    <h2 v-if="user">Hi, {{user.name}} {{user.surname}}</h2>
<h1 v-if="!user">You are not logged in</h1>
</div>
</template>

<script>
import axios from 'axios';
export default{
    name:'HomeComponent',
    data(){
        return {
            user:null
        }
    },
     created(){
        const response= axios.get('currentuser',{
            headers:{
                Authorization:'Bearer '+ localStorage.getItem('token')
            }
        });
        console.log(response);
        this.user=JSON.parse(window.localStorage.getItem('user'));
        console.log("AAAAAAAAA")
        console.log(this.user)
        
    }
}
</script>