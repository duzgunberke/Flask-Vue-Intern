
import Vuex from 'vuex';



const state ={
    user:null
};

const stores=new Vuex.Store({
    state,
    getters:{
        user:(state)=>{
            return state.user;
        }
    },
    actions:{
        user(context,user){
            context.commit('user',user);
        }
    },
    mutations:{
        user(state,user){
            state.user = user;
        }
    }
});

export default stores;