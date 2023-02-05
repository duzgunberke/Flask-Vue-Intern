<template>

    <form @submit.prevent="updateblog">
        <div class="form-outline mb-4">
            <label class="form-label" >Title</label>
            <p class="form-label bg-white">{{blog.title}}</p>
            <input type="text" required v-model="title" class="form-control" />
        </div>
    
        <div class="form-outline mb-4">
            <label class="form-label">Description</label>
            <p class="form-label bg-white">{{blog.description}}</p>

            <textarea class="form-control" required v-model="description" rows="4"></textarea>
        </div>
    
         <button class="btn btn-primary btn-block mb-4">Send</button>
    </form>
    
    
    </template>
        
    <script>
  import axios from "axios"
  import { useRoute } from "vue-router"
    
    export default {
      name: 'UpdateBlog',
      data(){
        return {
            blog:null,
            title:"",
            description: ""
        }
    },
      methods:{
        async updateblog(){
            const route = useRoute()
            const id = route.params.id
             const response = await axios.put(`/blog/${id}`,{ 
                        title:this.title,
                        description:this.description 
                });
                    console.log(response);
                    this.$router.push('/mypage');
        }},

    
    created(){
        const route = useRoute()
        const id = route.params.id
            axios.get(`/blog/${id}`)
            .then(response=>{
            console.log(response),
            this.blog=response.data.data
            });
            console.log(this.blog);  
        }

   }
    </script>