<template>
  <div id="app">
    <nav class="navbar">
      <a class="navbar-brand">
        <img src="https://i.ibb.co/r5krrdz/logo.png" height=40px alt="logo" @click="home">
      </a>
      <div v-if="isUserLogin">
        <li class="nitem"><router-link :to="{ name: 'MovieView' }">MovieView</router-link></li>
        <li class="nitem"><router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link></li>
        <li class="nitem"><router-link :to="{ name: 'LogInView' }">LogInPage</router-link></li>
        
      </div>
      <div v-else>
        <span id="uname">{{userName}}</span>
        <span id="uname2">님</span>
        <router-link :to="{ name: 'MyPageView' }" id="mPage">MyPage</router-link>
        <router-link :to="{ name: 'MbtiView' }" id="mbti">MyMBTI</router-link>
        <span @click="logout" id="lout">Logout</span>
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
    },
    home(){
      return this.$router.push({name: 'MovieView'})
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
/* body{
  background-image: url("https://user-images.githubusercontent.com/33485020/108069438-5ee79d80-7089-11eb-8264-08fdda7e0d11.jpg");
  
} */
body{
  background-color: black;
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

#uname{
  background-image: linear-gradient(90deg, purple, hotpink, crimson, orange, yellow);
  /* background-image: linear-gradient(90deg, red, orange, yellow, purple); */
  -webkit-background-clip: text;
  color: transparent;
  font-weight: bold;
  font-size: 27px;
  
}

#uname2{
  font-size: 13px;
  font-weight: bold;
  color: azure;
}

#mPage{
  margin-left: 27px;
  font-size: 23px;
  font-weight: bold;
  color: azure;
}

#mbti{
  margin-left: 27px;
  font-size: 23px;
  font-weight: bold;
  color: azure;
}

#lout{
  margin-left: 25px;
  font-size: 23px;
  font-weight: bold;
  color: azure;
  margin-right: 15px;
}


/* 1차 바꿈 */

</style>
