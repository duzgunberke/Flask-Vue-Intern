import axios from "axios";

axios.defaults.baseURL="http://192.168.40.144:5000/";
axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('token');