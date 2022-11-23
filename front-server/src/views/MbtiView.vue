<template>
 <div>
  <div class="back"></div>
  <!-- <img id="img2" src="https://s1.best-wallpaper.net/wallpaper/m/1206/Bear-toy-in-Toy-Story-3_m.jpg" alt=""> -->
  <div id="mbtibox">
    <br><br>
    <h1 id="qid">Q.</h1>
    <br><br><br>
    <h2 id="titleid">{{ title }}</h2>
    <br><br><br><br><br><br><br><br><br>
    <div class="a">
    <button  @click="findType(1)" class="btn btn-light" id="choicebtn">{{ choice1 }}</button >
    </div>
    <div class="a">
    <button  @click="findType(-1)" class="btn btn-light" id="choicebtn">{{ choice2 }}</button >
    </div>
  </div>
  <!-- <img id="img1" src="https://p4.wallpaperbetter.com/wallpaper/760/67/719/monsters-inc-movies-wallpaper-preview.jpg" alt=""> -->
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
 name: 'MbtiView',
 data(){
  return {
    num: 1,
    title: null,
    type: null,
    choice1: null,
    choice2: null,
    EI: 0,
    NS: 0,
    FT: 0,
    JP: 0,
    result: "",
  }
 },
 created(){
  this.getMbti()
 },
 methods: {
  findType(pm){
    this.num++
    if(this.num < 13){
      if (this.type == "EI"){
        this.EI = this.EI + pm
      }
      else if (this.type == "NS"){
        this.NS = this.NS + pm
      }
      else if (this.type == "FT"){
        this.FT = this.FT + pm
      }
      else {
        this.JP = this.JP + pm
      }
      this.getMbti()
    }
    else{
      this.getResult()
    }
  },
  getMbti(){
    axios({
      method: 'get',
      url: `${API_URL}/api/movies/mbti/${this.num}/`
    })
    .then(res => {
      this.title = res.data.title
      this.type = res.data.type
      this.choice1 = res.data.choice1
      this.choice2 = res.data.choice2
      // console.log(this.title)
    })
    .catch(err => {console.log(err)})
  },
  getResult(){
    if(this.EI > 0){
      this.result = this.result + "E"
    }
    else{
      this.result = this.result + "I"
    }
    if(this.NS > 0){
      this.result = this.result + "N"
    }
    else{
      this.result = this.result + "S"
    }
    if(this.FT > 0){
      this.result = this.result + "F"
    }
    else{
      this.result = this.result + "T"
    }
    if(this.JP > 0){
      this.result = this.result + "J"
    }
    else{
      this.result = this.result + "P"
    }
    this.$store.commit('GET_MBTI', this.result)
  }
 }

}
</script>

<style scoped>
div.back {
  background-color: black;
  z-index: -1;
}


#qid{
  color: #ECE3E3;
  font-size: 75px;
  float: left;
  margin-left: 30px;
  font-weight: bold;
  
}

#titleid{
  color: #ECE3E3;
  float: left;
  margin-left: 30px;
  margin-right: 30px;
  /* font-weight: bold; */
  font-size: 37px;
  /* -webkit-background-clip: text;
  color: transparent;
  text-shadow: -1px 0 lightgrey, 0 1px rgb(28, 27, 27), 1px 0 rgb(94, 85, 85); */
}

#mbtibox{
  background-color: rgb(16, 15, 15);
  width: 500px;
  height: 660px;
  margin-left: 700px;
  /* margin-top: 100px; */
  /* position: absolute;
  left: 35%;
  bottom: 10%; */
  /* float: left; */
  border-radius: 30px;
  border: 5px solid red;
  margin-top: 85px;
  /* display: flex;
  justify-content: center; */
  
}

#choicebtn{
  margin: 5px;
  width: 400px;
  padding: 20px;
  border-radius: 15px;
  /* border: 0.5px solid; */
  font-size: 20px;
  color: black;
  font-weight: bold;

}

.a button {
  transition: all 0.2s linear;
}
.a:hover button {
  transform: scale(1.05);
  background-color: red;
  border: 5px solid red;
  color: white;
}

#img1{
  position: absolute;
  left: 60%;
  bottom: 5%;
  /* right: 10px; */
  /* bottom: 50px; */
  width: 700px;
  z-index: -1;
}

/* #img2{
  float: left;
  padding-top:310px;
  margin-left: 70px;
  width: 700px;
  
} */



/* 수정함 */

</style>