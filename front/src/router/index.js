import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import SearchHistory from '../views/matchhistory/SearchHistory.vue'
import MatchHistory from '../views/matchhistory/MatchHistory.vue'
import CharacterList from '../views/gamedata/CharacterList.vue'
import CharacterDetail from '../views/gamedata/CharacterDetail.vue'
import NotFoundPage from '../views/NotFoundPage.vue'
import SelectCategory from '../views/gamedata/SelectCategory.vue'
import WeaponCategory from '../views/gamedata/WeaponCategory.vue'
import Category from '../views/gamedata/Category.vue'
import ItemDetail from '../views/gamedata/ItemDetail.vue'
import News from '../views/News.vue'
import MatTest from '../views/gamedata/MapList.vue'
import MapDetail from '../views/gamedata/MapDetail.vue'
import AnimalList from '../views/gamedata/AnimalList.vue'
import AnimalDetail from '../views/gamedata/AnimalDetail.vue'
import Ranking from '../views/open_api/Ranking.vue'
import PlayThroughList from '../views/community/PlayThroughList.vue'

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
    path: '/matchhistory',
    name: 'SearchHistory',
    component: SearchHistory
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
  {
    path: '/item/category',
    name: 'SelectCategory',
    component: SelectCategory
  },
  {
    path: '/item/category/weapon',
    name: 'WeaponCategory',
    component: WeaponCategory
  },
  {
    path: '/item/category/:category',
    name: 'Category',
    component: Category
  },
  {
    path: '/item/detail/:pk',
    name: 'ItemDetail',
    component: ItemDetail
  },
  {
    path: '/news',
    name: 'News',
    component: News
  },
  {
    path: '/mapdata',
    name: 'mapdata',
    component: MatTest
  },
  {
    path: '/mapdata/:pk',
    name: 'MapDetail',
    component: MapDetail
  },
  {
    path: '/animal',
    name: 'AnimalList',
    component: AnimalList
  },
  {
    path: '/animal/:pk',
    name: 'AnimalDetail',
    component: AnimalDetail
  },
  {
    path: '/rank',
    name: 'Ranking',
    component: Ranking
  },
  {
    path: '/playthroughlist',
    name: 'PlayThroughList',
    component: PlayThroughList
  },
  {
    path: '/notfound',
    name: 'NotFoundPage',
    component: NotFoundPage
  },
  {
    path: '*',
    redirect: '/notfound'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
