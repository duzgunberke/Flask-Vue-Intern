import axios from "axios";

axios.defaults.baseURL="http://192.168.0.18:5000/";
axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('token');
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';