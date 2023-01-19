<template>
    <div>
        
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
//import axios from 'axios';

export default {
    name: 'SettingsComponent',
    computed: {
        ...mapGetters(['user'])
    },

}
</script>