import Vue from 'vue'
import App from './App.vue'
import VueMaterial from 'vue-material'
import VueRouter from 'vue-router'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import Accueil from './components/Accueil.vue'

Vue.config.productionTip = false

Vue.use(VueMaterial)
Vue.use(VueRouter)

const router = new VueRouter ({
  routes : [ 
     {
       path: '/',
       component: Accueil 
     },
     {
       path: '/accueil',
       component: Accueil 
     },
  ],
  mode : 'history'
}) 

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
