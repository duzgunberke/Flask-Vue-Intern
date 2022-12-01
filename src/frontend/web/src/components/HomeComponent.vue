<template>
<h1>Hello</h1>
</template>

<script>
import axios from 'axios';
export default{
    name:'HomeComponent',
    async created(){
        const response=await axios.get('user');
        console.log(response);
    }
}
</script>