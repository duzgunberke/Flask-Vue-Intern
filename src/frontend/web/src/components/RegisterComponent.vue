<template>
    <form @submit.prevent="handleSubmit">
        <h3>Sign Up</h3>
        <div class="form-group">
            <label>Name</label>
            <input type="text" class="form-control" required v-model="name" placeholder="Name" />
        </div>
        <div class="form-group">
            <label>Surname</label>
            <input type="text" class="form-control" required v-model="surname" placeholder="Surname" />
        </div>
        <div class="form-group">
            <label>Username</label>
            <input type="text" class="form-control" required v-model="username" placeholder="Username" />
        </div>
        <div class="form-group">
            <label>Email</label>
            <input type="email" class="form-control" required v-model="email" placeholder="Email" />
        </div>
        <div class="form-group">
            <label>Password</label>
            <input type="password" class="form-control" required v-model="password" placeholder="Password" />
        </div>
        <button class="btn btn-primary btn-block">Sign Up Now</button>
    </form>
</template>

<script>
import axios from "axios"

export default{
    name:'RegisterComponent',
    data(){
      return{
        name:'',
        surname:'',
        username:'',
        password:'',
        email:''
      }
    },
    methods:{
        async handleSubmit(){
          const response = await axios.post('signup',{ 
                name:this.name,
                surname: this.surname,
                username: this.username,
                password: this.password,
                email: this.email
          });
            console.log(response);
            this.$router.push('/login');
        }
    }
}
</script>