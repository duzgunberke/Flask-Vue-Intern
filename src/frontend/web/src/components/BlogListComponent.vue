<template>
<div class="row">
  <div class="col-sm-3 p-2" v-for="blog in blogs" v-bind:key="blog.id">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">{{ blog.title }}</h5>
        <p class="card-text">{{blog.description}}</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div>
    </div>
  </div>
</div>
    </template>
    
    <script>
      import axios from "axios"
//import {getAllBlogs} from '../Functions'
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