import axios from "axios";

axios.defaults.baseURL="http://192.168.0.8:5000/";
axios.defaults.headers.common['Authorization'] =localStorage.getItem('token');
axios.defaults.headers.common['Content-Type'] = 'application/json';
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';