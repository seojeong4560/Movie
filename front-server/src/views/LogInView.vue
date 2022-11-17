<template>
  <div id="Loginbox">
  <form @submit.prevent="logIn">
  <h1 id="LogInPage">LogIn Page</h1>
  <div class="mb-3">
      <label for="username" id= "username" class="form-label">username</label>
      <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" v-elseid="username" v-model="username"><br>
      <div id="emailHelp" class="form-text" style="color: #8c8c8c">We'll never share your email with anyone else.</div>
  </div>
  <div class="mb-3">
      <label for="password" id="password" class="form-label"> password</label>
      <input type="password" class="form-control" id="password" v-model="password" ><br>
  </div>
      <input id="submit_logIn" type="submit" value="logIn" class="btn btn-danger" >
  </form>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return{
      username: null,
      password: null,
    }
  },
  methods: {
    logIn(){
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn', payload)
    }
  }
}
</script>

<style>
#Loginbox{
  width: 600px;
  height: 500px;
  background-color: black;
  background-color: rgba( 0, 0, 0, 0.8 );
  margin: auto;
}

#LogInPage{
  padding: 25px;
  color: aliceblue;
  font-weight: bold;
  
}

#username{
  color: #8c8c8c;
  font-size: 20px;
  font-weight: bold;
}

#password{
  color: #8c8c8c;
  font-size: 20px;
  font-weight: bold;
}

.form-control{
  width: 400px;
  height: 45px;
  background-color: #333333;
  background-color: rgb(50, 50, 50, 1.5);
  border-color: #333333;
  
  margin: auto;
}

#submit_logIn {
  margin-top: 20px;
  width: 400px;
  height: 45px;
  background-color: red;
}
</style>