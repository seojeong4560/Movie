<template>
  <div>
    <div class="back"></div>
    <br><br>
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
    <img src="https://t1.daumcdn.net/cfile/tistory/2255384755AA0EB02C" alt="">
    <br><br>
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

<style scoped>
div.back {
  /* width: 100vw;
  height: 90vh; */
  position: absolute;
  /* background-image: url("https://i.pinimg.com/originals/e9/54/b2/e954b2d4f79c1da0909f38f6050a30d7.jpg");  */
  background-repeat: no-repeat;
  z-index: -1;
  filter: brightness(55%);
  
  
}



#backimg{
  width: 1900px;
  height: 800px;
}

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