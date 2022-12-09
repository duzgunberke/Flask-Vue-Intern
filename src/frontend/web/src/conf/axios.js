import axios from "axios";

axios.defaults.baseURL="http://10.22.116.104:5000/";
axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('token');