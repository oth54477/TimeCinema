import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView'
import TimeLineView from '@/views/TimeLineView'
import MovieDetailView from '@/views/MovieDetailView'
import RecommendView from '@/views/RecommendView'
import ArticleView from '@/views/ArticleView'
import LogInView from '@/views/LogInView'
import SignUpView from '@/views/SignUpView'
import ProfileView from '@/views/ProfileView'
import UserListView from '@/views/UserListView'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faUserSecret)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/time',
    name: 'time',
    component: TimeLineView
  },
  {
    path: '/:id',
    name: 'detail',
    component: MovieDetailView
  },
  {
    path: '/recommend/:times',
    name: 'recommend',
    component: RecommendView
  },
  {
    path: '/article',
    name: 'article',
    component: ArticleView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'login',
    component: LogInView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/userList',
    name: 'userList',
    component: UserListView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
