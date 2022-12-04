<template>
<div>
    <h2 v-if="user">Hi, {{user.name}} {{user.surname}}</h2>
<h1 v-if="!user">You are not logged in</h1>
</div>
</template>

<script>
//import {mapGetters} from 'vuex'
export default{
    name:'HomeComponent',
    props:['user']
    // ,computed: {
    //     ...mapGetters(['user'])
    // }

}
</script>