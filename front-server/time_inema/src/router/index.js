import Vue from 'vue'
import VueRouter from 'vue-router'
import TimeLineView from '@/views/TimeLineView'
import MovieDetailView from '@/views/MovieDetailView'
import RecommendView from '@/views/RecommendView'

Vue.use(VueRouter)

const routes = [
  // {
  //   path: '/',
  //   name: 'home',
  //   component: HomeView
  // },
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
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
