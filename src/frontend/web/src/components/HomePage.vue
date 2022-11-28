<template>
    <div>
        <h5  class="text-center">{{ msg }}</h5>
    </div>
</template>

<script>
import axios from 'axios';

export default{
    name: 'HomePage',
    data(){
        return{
            msg : ""
        };
    },
    methods : {
        getReponse(){
            const path="http://localhost:5000/blogs";
            axios.get(path)
            .then ((res)=> {
                console.log(res.data)
                this.msg=res.data;
            })
            .catch ((err)=>{
                console.log(err)
            });
        },
    },
    created(){
        this.getReponse();
    }
}
</script>