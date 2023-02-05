<template>
    <h2>The author of the blogs here : {{ id }}</h2>
    <div class="row">
        <div class="col-sm-3 p-2" v-for="blog in blogs" v-bind:key="blog._id">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">{{ blog.title }}</h5>
                    <p class="card-text">{{ blog.description.substring(0, 60) }}...</p>
                    <a v-bind:href="'/blogdetail/' + blog._id" class="btn btn-primary">Details...</a>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
  import { onMounted } from "vue"
  import axios from "axios"
  import { useRoute } from "vue-router"
export default {
    name: 'AuthorBlogs',

    setup(){
        const route = useRoute()
        const id = route.params.author
        const blogs=null
        onMounted(()=>{
            axios.get('/authorblogs',{id})
                    .then(response => {
                        this.blogs=response.data.data
                    })
        })
       
       return{
        id,blogs
       }
    }


}
</script>