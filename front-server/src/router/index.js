import Vue from 'vue'
import VueRouter from 'vue-router'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import MyPageView from '@/views/MyPageView'
import MovieView from '@/views/MovieView'
import DetailView from '@/views/DetailView'
import MbtiView from '@/views/MbtiView'
import MbtiResultView from '@/views/MbtiResultView'
import CheckListView from '@/views/CheckListView'


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
    path: '/mbti',
    name: 'MbtiView',
    component: MbtiView
  },
  {
    path: '/mbtiresult',
    name: 'MbtiResultView',
    component: MbtiResultView
  },
  {
    path: '/checklist',
    name: 'CheckListView',
    component: CheckListView
  },

  // id가 다른 router 앞으로 가게 되면 먼저 인식이 되어 버린다.
  {
    path: '/:id',
    name: 'DetailView',
    component: DetailView
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
