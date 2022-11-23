<template>
 <div>
  <div class="back"></div>
  <br>
    <h1 id="qid">Q.</h1>
    <h2 id="titleid">{{ title }}</h2>
    <br>
    <div class="a" id="cbtn1">
      <img src="https://img.etnews.com/cms/uploadfiles/afieldfile/2013/09/16/477971_20130916112920_346_0001.jpg" alt="">
    <button  @click="findType(1)" class="btn btn-light" id="choicebtn">{{ choice1 }}</button >
    </div>
    <div class="a" id="cbtn2">
      <img src="https://img.insight.co.kr/static/2021/07/02/700/img_20210702112100_f33w552m.webp" alt="">
    <button  @click="findType(-1)" class="btn btn-light" id="choicebtn">{{ choice2 }}</button >
    </div>
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
  /* float: left; */
  margin-right: 550px;
  font-weight: bold;
  
}

#titleid{
  color: #ECE3E3;
  font-weight: bold;
  /* margin-left: 30px; */
  /* margin-right: 30px; */
  /* font-weight: bold; */
  font-size: 37px;
  /* -webkit-background-clip: text;
  color: transparent;
  text-shadow: -1px 0 lightgrey, 0 1px rgb(28, 27, 27), 1px 0 rgb(94, 85, 85); */
}


img{
  width: 650px;
  border-radius: 30px;
  float: left;
}


#cbtn1{
  float: left;
  margin-left: 300px;
  width: 650px;
}

#cbtn2{
  float: left;
  margin-left: 20px;
  width: 650px;
}

#choicebtn{
  margin: 5px;
  width: 650px;
  padding: 20px;
  border-radius: 15px;
  /* border: 0.5px solid; */
  font-size: 20px;
  color: black;
  font-weight: bold;

}

/* .a img{
  transition: all 0.5s linear;
}

.a:hover img{
  transform: scale(1.05);
}

.a button {
  transition: all 0.5s linear;
}
.a:hover button {
  transform: scale(1.05);
  background-color: red;
  border: 5px solid red;
  color: white;
} */

.a {
  transition: all 0.7s linear;
}

.a:hover {
  transform: scale(1.05);
  
}

.a:hover button {
  background-color: red;
  border: solid red;
} 





/* 수정함 */

</style>