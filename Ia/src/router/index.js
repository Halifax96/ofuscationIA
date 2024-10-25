import Vue from 'vue'
import VueRouter from 'vue-router'
import Portada from '../views/Portada.vue'
import Principal from '../views/Principal.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Portada
  },
  {
    path: '/principalia',
    name: 'principal',
    component: Principal
  }
]

const router = new VueRouter({
  routes
})

export default router
