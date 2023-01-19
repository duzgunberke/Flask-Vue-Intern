<template>
    <div>
        <section class="vh-100">
        <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-70">
                <div class="col col-xxxl-10">
                    <div class="row g-0">
                        <div class="col-md-6 col-lg-8 d-flex align-items-center">
                            <div class="input-group">

                            </div>
                        </div>
                    </div>
                    <h1>{{ title }}</h1>
                    <hr>
                    <h3>{{ description }}</h3>
                    <br>
                    <h2>Author : <a v-bind:href="'/authorblogs/'+ author">{{ author }}</a></h2>
                    <hr>
                </div>
            </div>
        </div>
    </section>
    </div>
  </template>
      
  <script>
  import { onMounted, ref } from "vue"
  import axios from "axios"
  import { useRoute } from "vue-router"

  export default {
    name: 'BlogDetail',
    setup(){
        const route = useRoute()
        const id = route.params.id
        const title=ref("");
        const description = ref("");
        const author = ref("");
        onMounted(()=>{
            axios.post('getblogbyid',{id})
                    .then(response => {
                        title.value = response.data.title
                        description.value = response.data.description
                        author.value = response.data.author
                    })
        })
       
       return{
        title,description,author
       }
    }
  
  }
  </script>