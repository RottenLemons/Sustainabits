import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import SignUpView from '../views/SignUpView.vue'
import DataView from '../views/DataView.vue'
import ReferenceView from '../views/ReferenceView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: {
        hideLoginSignBtns: false,
      }   
    },
    {
      path: '/ref',
      name: 'references',
      component: ReferenceView,
      meta: {
        hideLoginSignBtns: true,
      }   
    },
    {
      path: '/data',
      name: 'data',
      component: DataView,
      meta: {
        hideLoginSignBtns: true,
      }   
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      meta: {
        hideLoginSignBtns: true,
      }      
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView,
      meta: {
        hideLoginSignBtns: true,
      }      
    }
  ]
})

export default router
