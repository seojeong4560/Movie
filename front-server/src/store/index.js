import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  state: {
    upcomming_movies : [],
    latest_movies : [],
    highscore_movies : [],
    like_movies : [],
    genres: [],
    checked_genres: [],
    token: null,
    username: null,
    mbti: null,
    mbti_genres: []
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
      state.upcomming_movies = movieList.upcomming_movies
      state.latest_movies = movieList.latest_movies
      state.highscore_movies = movieList.highscore_movies
      state.like_movies = movieList.like_movies
      // console.log(state.latest_movies)
    },
    GET_GENRE_LIST(state, genres){
      state.genres = genres.genres
    },
    SAVE_TOKEN(state, name_token){
      state.username = name_token.username
      state.token = name_token.token
      router.push({name: 'MovieView'})
    },
    LOGOUT(state){
      state.token = !state.token
      state.username = null
      router.push({name: 'MovieView'})
    },
    GET_MBTI(state, payload){
      console.log(payload)
      state.mbti = payload.result
      state.mbti_genres = payload.genres
      router.push({name: 'MbtiResultView'})
    }
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
    getGenreList(context){
      axios({
        method: 'get',
        url: `${API_URL}/api/movies/recommend/`
      })
      .then((res) => {
        context.commit('GET_GENRE_LIST', res.data)
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
    },
  },
  modules: {
  }
})
