<template>
  <div id="app">
    <nav class="navbar">
      <a class="navbar-brand" href="#">
        <img src=""  height=70px alt="logo">
      </a>
      <div v-if="isUserLogin">
        <li class="nitem"><router-link :to="{ name: 'MovieView' }">MovieView</router-link></li>
        <li class="nitem"><router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link> | </li>
        <li class="nitem"><router-link :to="{ name: 'LogInView' }">LogInPage</router-link></li>
        
      </div>
      <div v-else>
        <span>{{userName}}님</span>
        <router-link :to="{ name: 'MyPageView' }">MyPage</router-link>
        <button @click="logout">Logout</button>
      </div>
    </nav>
  <router-view :key="$route.fullPath"></router-view>

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
body{
  background-image: url("D:\Desktop\final_pjt\final_pjt\front-server\src\assets\background.jpg")
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  margin: 20px;
  display: flex;
  justify-content: space-between;
  padding: 30px;
  display: grid;
  grid-template-columns: 600px 1fr;
  text-align: center;
  
}

.nitem{
  display: flex;
  float: left;
  padding: 15px;
}

nav a {
  text-decoration: none;
  font-weight: bold;
  color: white;
  font-size: 20px;
}

nav a.router-link-exact-active {
  color: red;
}
</style>
