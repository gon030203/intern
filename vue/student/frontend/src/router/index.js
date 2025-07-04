import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '../views/LoginPage.vue'
import Dashboard from '../views/Dashboard.vue'

const routes = [
  { path: '/', component: LoginPage },
  { path: '/dashboard', 
    component: Dashboard,
    beforeEnter: (to, from, next) => {
        const token = localStorage.getItem('token')
        if (!token) {
          next('/')
        } else {
          next()
        }
      }
    }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router