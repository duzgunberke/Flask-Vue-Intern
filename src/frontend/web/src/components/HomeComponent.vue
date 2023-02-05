<template>
    <div>
        <h2 v-if="user">{{ user.name }} {{ user.surname }}</h2>
        <h1 v-else>You are not logged in</h1>

    </div>
    <div v-if="role!='user'">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Title</th>
                    <th scope="col">Update</th>
                    <th scope="col">Delete</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="blog in blogs" v-bind:key="blog._id">
                    <th scope="row">#</th>
                    <td>{{blog.title}}</td>
                    <td>

                        <a class="btn btn-warning" v-bind:href="'/updateblog/'+ blog._id">Update</a>
                    </td>
                    <td>
                         <a class="btn btn-danger" @click="deleteSubmit(blog._id)">Delete</a>
                    </td>
                </tr>
            </tbody>
        </table>
        <router-link  class="btn btn-primary" to="/addblog">New Blog</router-link>
    </div>
    <div v-else>
        <h1>You are not author ! </h1>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
import axios from 'axios';

export default {
    name: 'HomeComponent',
    computed: {
        ...mapGetters(['user']),
        role() {
      return this.user.role
    }
    },
    methods:{
        deleteSubmit(id){
      axios.delete(`blog/${id}` ,{
        headers: { Authorization:'Bearer ' + localStorage.getItem('token')}
      })
      
      this.$router.push('/');
    },
    updateSubmit(id){
      axios.get(`blog/${id}` ,{
        headers: { Authorization:'Bearer ' + localStorage.getItem('token')}
      })
      
      this.$router.push('/');
    }
    },
    
    data(){
        return {
            blogs:null
        }
    },
     created(){
            
         axios.get('blogbyauthor',{
            headers:{
                Authorization:'Bearer ' + localStorage.getItem('token')
            }
         })
        .then(response=>{
          console.log(response),
          this.blogs=response.data.data
        });
        console.log(this.blogs);

    }
  

}
</script>