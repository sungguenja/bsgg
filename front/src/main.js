import Vue from 'vue'
import App from './App.vue'
import router from './router'
// bootstrap-vue
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
// bootstrap and bootstrap-vue css
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false

// bootstrap-vue set
Vue.use(BootstrapVue)
// Icons
Vue.use(IconsPlugin)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
