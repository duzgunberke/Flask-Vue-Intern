import axios from "axios";

axios.defaults.baseURL=process.env.VUE_API_URL;
axios.defaults.headers.common['Authorization'] = process.env.VUE_API_HEADER;
axios.defaults.headers.common['Content-Type'] = 'application/json';
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';