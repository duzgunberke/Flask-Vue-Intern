<template>
    <form @submit.prevent="handleSubmit">
        <h3>Login</h3>
        <div class="form-group">
            <label>Username</label>
            <input type="text" class="form-control" v-model="username" placeholder="Username" />
        </div>
        <div class="form-group">
            <label>Password</label>
            <input type="password" class="form-control" v-model="password" placeholder="Password"  />
        </div>
        <button class="btn btn-primary btn-block">Login</button>
    </form>
</template>
    
    <script>
    import axios from "axios"
    export default{
        name:'LoginComponent',
        data(){
            return{
              username:'',
              password:''
            }
        },
        methods: {
            async handleSubmit(){
                const response =await axios.post('login',{
                    username:this.username,
                    password:this.password
                });
                console.log(response);
                
                localStorage.setItem('token',response.data.token);
                window.localStorage.setItem('user',JSON.stringify(response.data.user))
                this.$router.push('/mypage');
            }
        }
    }
    </script>