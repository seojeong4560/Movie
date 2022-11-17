<template>
  <div id="app">
    <nav class="navbar bg-black">
      <a class="navbar-brand" href="#">
        <img src="/.assets/netflixlogo.png" height=70px alt="">
      </a>
      <router-link :to="{ name: 'MovieView' }">MovieView</router-link>
      <div v-if="isUserLogin">
        <router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link> | 
        <router-link :to="{ name: 'LogInView' }">LogInPage</router-link>
      </div>
      <div v-else>
        <span>{{userName}}님</span>
        <router-link :to="{ name: 'MyPageView' }">MyPage</router-link>
        <button @click="logout">Logout</button>
      </div>
    </nav>
  <router-view/>

  </div>
</template>

<script>
export default {
  name: 'App',
  components:{
    // MovieView
  },
  computed: {
    userName(){
      return this.$store.state.username
    },
    isUserLogin(){
      return !this.$store.getters.isLogin
    }
  },
  methods: {
    logout(){
      this.$store.commit('LOGOUT')
    },
    새창 () {
      localStorage.setItem('vuex', sessionStorage.getItem('vuex')) // vuex session to local
    }
  },
  beforeCreate () {
    let localVuex = localStorage.getItem('vuex') // local storage에 vuex 저장여부 확인
    if (localVuex) { // 저장되어 있는 경우 session storage로 이동 후 local 제거
      localVuex = JSON.parse(localVuex)
      this.$store.commit('setXXX', localVuex.xxx)
      localStorage.removeItem('vuex') 
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
