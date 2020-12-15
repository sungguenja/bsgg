import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import MatchHistory from '../views/matchhistory/MatchHistory.vue'
import CharacterList from '../views/gamedata/CharacterList.vue'
import CharacterDetail from '../views/gamedata/CharacterDetail.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/matchhistory/:user_name/:season/:team_mode',
    name: 'MatchHistory',
    component: MatchHistory
  },
  {
    path: '/characters',
    name: 'CharacterList',
    component: CharacterList
  },
  {
    path: '/characters/:pk',
    name: 'CharacterDetail',
    component: CharacterDetail
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router