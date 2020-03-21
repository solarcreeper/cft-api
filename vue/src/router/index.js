import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Home from '../views/Home.vue'
import Welcome from '../views/Welcome.vue'
import Io from '../views/Io.vue'
import Scripts from '../views/Scripts.vue'
import StrategyEngine from '../views/StrategyEngine.vue'
import HisIo from '../views/HisIo.vue'
import HisScripts from '../views/HisScripts.vue'
import Report from '../views/Report.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/login', component: Login },
  { path: '/', redirect: '/login' },
  {
    path: '/home',
    component: Home,
    redirect: '/welcome',
    children: [
      { path: '/welcome', component: Welcome },
      { path: '/io', component: Io },
      { path: '/scripts', component: Scripts },
      { path: '/strategy', component: StrategyEngine },
      { path: '/his_io', component: HisIo },
      { path: '/his_scripts', component: HisScripts },
      { path: '/report', component: Report }
    ]
  }
]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  if (to.path === '/login') {
    return next()
  }
  const tokenStr = window.sessionStorage.getItem('token')
  if (!tokenStr) {
    return next('/login')
  }
  next()
})

export default router
