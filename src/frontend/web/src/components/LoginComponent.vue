<template>
    <form @submit.prevent="handleSubmit">
        <div v-if="error" class="alert alert-danger" role="alert">
            {{error}}
        </div>
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
              password:'',
              error:''
            }
        },
        methods: {
            async handleSubmit(){
                try{
                    const response =await axios.post('login',{
                    username:this.username,
                    password:this.password
                });
                console.log(response);
                if(response.data.message){
                    this.error=response.data.message
                }
                else{

                    localStorage.setItem('token',response.data.token);
                    //window.localStorage.setItem('user',JSON.stringify(response.data.user))
                    this.$store.dispatch('user',response.data.user);
                    this.$router.push('/mypage');
                }
                }catch(e){
                    this.error="Invalid username/password !"
                }
                
            }
        }
    }
    </script>