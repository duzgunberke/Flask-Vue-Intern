<template>
    
    <div v-if="role='admin'">
        <h1>WELCOME THE ADMIN PAGE</h1>
    </div>
    <div v-if="role=='admin'">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Username</th>
                    <th scope="col">Name</th>
                    <th scope="col">Email</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="person in users" v-bind:key="person.id">
                    <th scope="row">#</th>
                    <td>{{person.username}}</td>
                    

                        <td>{{person.name}}</td>
                    
                    
                        <td>{{person.email}}</td>

                </tr>
            </tbody>
        </table>
        
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
import axios from 'axios';

export default {
    name: 'UserList',
    computed: {
        ...mapGetters(['user']),
         role() {
      return this.user.role
    }
    },
    methods:{
     
    },
    
    data(){
        return {
            users:null
        }
    },
     created(){
            
         axios.get('users',{
            headers:{
                Authorization:'Bearer ' + localStorage.getItem('token')
            }
         })
        .then(response=>{
          console.log(response),
          this.users=response.data
        });
        console.log(this.users);
    }
  

}
</script>