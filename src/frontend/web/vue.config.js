const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer:{
    proxy:{
      'V1':{
        target: 'http://192.168.0.18:5000/',
        changeOrigin:true,
        ws:true
      }
    }
  }
})
