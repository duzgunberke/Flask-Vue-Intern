<template>
      <form @submit.prevent="updateUser">
        <div class="form-outline mb-4">
            <label class="form-label" >Username : </label>
            <p class="form-label bg-white">{{user.username}}</p>
        </div>
    
        <div class="form-outline mb-4">
            <label class="form-label">First Name :</label>
            <p class="form-label bg-white">{{user.name}}</p>
            <input class="form-control" required v-model="name" />
        </div>
    
        <div class="form-outline mb-4">
            <label class="form-label">Surname :</label>
            <p class="form-label bg-white">{{user.surname}}</p>
            <input class="form-control" required v-model="surname" />
        </div>
    
        <div class="form-outline mb-4">
            <label class="form-label">Email :</label>
            <p class="form-label bg-white">{{user.email}}</p>
            <input class="form-control" required v-model="email" />
        </div>
    
         <button class="btn btn-primary btn-block mb-4">Update</button>
    </form>
</template>

<script>
import { mapGetters } from 'vuex'
import axios from "axios"

export default {
    name: 'SettingsComponent',
    computed: {
        ...mapGetters(['user'])
    },
    data(){
        return {
            name:"",
            surname: "",
            email:""
        }
    },
      methods:{
        async updateUser(){
           
             const response = await axios.put(`/edituser`,{ 
                        name:this.name,
                        surname:this.surname,
                        email:this.email 
                });
                    console.log(response);
                    this.$router.push('/mypage');
        }}
}
</script>