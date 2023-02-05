const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer:{
    proxy:{
      'V1':{
        target: process.env.VUE_API_URL,
        changeOrigin:true,
        ws:true
      }
    }
  }
})
