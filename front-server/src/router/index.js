import Vue from 'vue'
import VueRouter from 'vue-router'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import MyPageView from '@/views/MyPageView'
import MovieView from '@/views/MovieView'
import DetailView from '@/views/DetailView'
import MbtiView from '@/views/MbtiView'
import MbtiResultView from '@/views/MbtiResultView'


Vue.use(VueRouter)

const routes = [
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },

  {
    path: '/mypage',
    name: 'MyPageView',
    component: MyPageView
  },

  {
    path: '/',
    name: 'MovieView',
    component: MovieView
  },

  {
    path: '/:id',
    name: 'DetailView',
    component: DetailView
  },

  {
    path: '/mbti',
    name: 'MbtiView',
    component: MbtiView
  },
  {
    path: '/mbtiresult',
    name: 'MbtiResultView',
    component: MbtiResultView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
// router.beforeEach((to, from, next) => {
//   console.log('to', to)
//   console.log('from', from)
//   console.log('next', next)
//   next()
// })
export default router
