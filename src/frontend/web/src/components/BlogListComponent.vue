<template>
<div class="row">
  <div class="col-sm-3 p-2" v-for="blog in blogs"  v-bind:key="blog._id">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">{{ blog.title }}</h5>
        <p class="card-text">{{blog.description.substring(0,60)}}...</p>
            <a v-bind:href="'/blogdetail/'+ blog._id" class="btn btn-primary">Details...</a>

      </div>
    </div>
  </div>
</div>
    </template>
    
    <script>
      import axios from "axios"
    export default{
        name:'BlogListComponent',
        data(){
        return {
            blogs:null
        }
    },
     created(){
 
         axios.get('/blogs')
        .then(response=>{
          console.log(response),
          this.blogs=response.data.data
        });
        console.log(this.blogs);  
    }
  
    
    }
    </script>