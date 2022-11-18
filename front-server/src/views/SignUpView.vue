<template>
  <div>
    <h1 id="SignUpPageMessage">Unlimited movies, TV shows, and more.</h1>
    <h2 id="SignUpPageMessage2">Watch anywhere. Cancel anytime.</h2>
    <h3 style="color: white; font-size: 20px">Ready to watch? Enter your email to create or restart your membership.</h3>
    <form @submit.prevent="signUp" id="formsignup">
      <label for="username"></label>
      <input type="text" id="username" placeholder="username" v-model="username" class="btn btn-light"><br>

      <label for="password1" ></label>
      <input type="password" id="password1" placeholder="password" v-model="password1" class="btn btn-light"><br>

      <label for="password2" ></label>
      <input type="password" id="password2" placeholder="password confirmation" v-model="password2" class="btn btn-light">
      <br>
      <input id="sigunUpbtn" type="submit" value="SignUp" class="btn btn-danger">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return{
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username: username,
        password1: password1,
        password2: password2,
      }
      this.$store.dispatch('signUp', payload)
    }
  }
}
</script>

<style>
/* body{
  background-image: url("https://user-images.githubusercontent.com/33485020/108069438-5ee79d80-7089-11eb-8264-08fdda7e0d11.jpg"); 
  
} */

#SignUpPageMessage{
  padding: 25px;
  color: aliceblue;
  font-weight: bold;
  font-size: 50px;
}

#SignUpPageMessage2{
  color: aliceblue;
  font-weight: bold;
  font-size: 30px;
}

#formsignup{
  padding: 40px;
}

#username{
  width: 400px;
  height: 40px;
  
}

#password1{
  margin: 5px;
  width: 400px;
  height: 40px;
}

#password2{
  width: 400px;
  height: 40px;
  margin-bottom: 10px;
}

#sigunUpbtn{
  width: 200px;
  background-color: red;
}

input::placeholder{
  font-size: 15px
}
</style>