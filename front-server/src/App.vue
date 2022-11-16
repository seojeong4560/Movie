<template>
  <div id="app">
    <nav>
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
    }
  }
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
