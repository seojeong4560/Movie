import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  state: {
    // movieLIst: [],
    latest_movies : [],
    highscore_movies : [],
    like_movies : [],
    token: null,
    username: null,
  },
  plugins: [
    createPersistedState({
      storage: window.sessionStorage // store를 session storage 에 유지
    })
  ],
  getters: {
    isLogin(state){
      return state.token ? true : false
    }
  },
  mutations: {
    GET_MOVIE_LIST(state, movieList){
      state.latest_movies = movieList.latest_movies
      state.highscore_movies = movieList.highscore_movies
      state.like_movies = movieList.like_movies
      // console.log(state.latest_movies)
    },
    SAVE_TOKEN(state, name_token){
      state.username = name_token.username
      state.token = name_token.token
      router.push({name: 'MovieView'})
    },
    LOGOUT(state){
      state.token = !state.token
      state.username = null
      router.push({name: 'LogInView'})
    },
  },
  actions: {
    getMovieList(context){
      axios({
        method: 'get',
        url: `${API_URL}/api/movies/`
      })
      .then((res) => {
        // console.log(res.data.highscore_movies)
        context.commit('GET_MOVIE_LIST', res.data)
      })
      .catch(err => {
        console.log(err)
      })
    },
    getMovieDetail(context){
      axios({
        method: 'get',
        url: `${API_URL}/api/movies/detail/${this.movieId}`
      })
      .then(res => {
        context.commit('GET_MOVIE_DETAIL',res)
      })
      .catch(err => { console.log(err) })
    },
    signUp(context, payload){
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
      .then((res) => {
        // console.log(res)
        context.commit('SAVE_TOKEN', res.data.key)
      })
    },
    logIn(context, payload){
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
      .then((res) => {
        // console.log(res)
        const name_token = {
          username: payload.username,
          token: res.data.key
        }
        context.commit('SAVE_TOKEN', name_token)
      })
    }
  },
  modules: {
  }
})
