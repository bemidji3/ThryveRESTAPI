import Vue from 'vue'
import App from './App.vue'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material-design-icons/styles.css'
import MenuIcon from 'vue-material-design-icons/Menu.vue';


Vue.config.productionTip = false
Vue.use(VueMaterial)


Vue.component('menu-icon', MenuIcon);


new Vue({
  render: h => h(App),
}).$mount('#app')
