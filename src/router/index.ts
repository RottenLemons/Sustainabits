import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import SignUpView from '../views/SignUpView.vue'
import CompetitionsView from '../views/CompetitionsView.vue'
import ActivityView from '../views/ActivityView.vue'
import ProfileView from '../views/ProfileView.vue'
import EventsView from '../views/EventsView.vue'
import UsersView from '@/views/UsersView.vue'
import TreesView from '@/views/TreesView.vue'
import CompView from '@/views/CompView.vue'
import CreateCompetition from '@/views/CreateCompetition.vue'

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
      path: '/users',
      name: 'users',
      component: UsersView,
      meta: {
        hideLoginSignBtns: false,
      }   
    }, 
    {
      path: '/ccomp',
      name: 'createCompetition',
      component: CreateCompetition,
      meta: {
        hideLoginSignBtns: false,
      }   
    }, 
    {
      path: '/trees',
      name: 'trees',
      component: TreesView,
      meta: {
        hideLoginSignBtns: false,
      }   
    },
    {
      path: '/activities',
      name: 'activities',
      component: ActivityView,
      meta: {
        hideLoginSignBtns: true,
      }   
    },
    {
      path: '/events',
      name: 'events',
      component: EventsView,
      meta: {
        hideLoginSignBtns: true,
      }   
    },
    {
      path: '/competitions',
      name: 'competitions',
      component: CompetitionsView,
      meta: {
        hideLoginSignBtns: true,
      }   
    },
    {
      path: '/comps/:compID?',
      name: 'comps',
      component: CompView,
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
    },

    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
      meta: {
        hideLoginSignBtns: true,
      }      
    }
  ]
})

export default router
