<template>
<div class="row">
  <div class="col-sm-3 p-2" v-for="blog in blogs"  v-bind:key="blog._id">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">{{ blog.title }}</h5>
        <p class="card-text">{{blog.description.substring(0,60)}}...</p>
        <!-- <a href="javascript:void(0)" @click="getdetailClick(blog.id)" class="btn btn-primary">Details...</a> -->
            <a v-bind:href="'/blogdetail/'+ blog._id" class="btn btn-primary">Details...</a>

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
        methods:{
          getdetailClick(_id){
            const blogId = JSON.stringify({ "id": _id });
              const response=axios.post("getblogbyid", blogId);
              console.log(response)
                         
          }
        },
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