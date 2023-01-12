<template>

<form v-on:submit.prevent="submitForm">
    <div class="form-outline mb-4">
        <label class="form-label" >Title</label>
        <input type="text" required v-model="form.title" class="form-control" />
    </div>

    <div class="form-outline mb-4">
        <label class="form-label">Description</label>
        <textarea class="form-control" required v-model="form.description" rows="4"></textarea>
    </div>

     <button class="btn btn-primary btn-block mb-4">Send</button>
</form>


</template>
    
<script>
//import {mapGetters} from 'vuex'
import axios from "axios"

export default {
  name: 'AddOrUpdateBlog',
  
  data(){
        return{
            form: {
                title: '',
                description: ''
            }
        }
    },
    methods:{
        submitForm(){
            axios.post('/addblog', this.form,{
        headers: { Authorization:'Bearer ' + localStorage.getItem('token')}
      })
                 .then((res) => {
                     console.log(res)
                 })
                 .catch((error) => {
                     console.log(error)
                 });
                 this.$router.push('/mypage');
        }

}}
</script>