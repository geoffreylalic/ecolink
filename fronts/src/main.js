import Vue from 'vue'
import App from './App.vue'
import VueMaterial from 'vue-material'
import VueRouter from 'vue-router'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import Accueil from './components/Accueil.vue'
import Annonce from './components/Annonce.vue'
import DeposerAnnonce from './components/DeposerAnnonce.vue'
import ListingAnnonces from './components/ListingAnnonces.vue'
import APropos from './components/APropos.vue'
import CreerCompte from './components/CreerCompte.vue'

Vue.config.productionTip = false

Vue.use(VueMaterial)
Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
    {
      path: '/',
      component: Accueil
    },
    {
      path: '/accueil',
      component: Accueil
    },
    {
      path: '/deposerannonce',
      component: DeposerAnnonce
    },
    {
      path: '/annonces',
      component: ListingAnnonces,
    }, 
    {
      path: '/apropos',
      component: APropos
    },
    {
      path:'/creercompte',
      component: CreerCompte
    },
    {
      name :'Annonce',
      path:'/annonce/:id',
      component: Annonce,
    }
  ],
  mode: 'history'
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
