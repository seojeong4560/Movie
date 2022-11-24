<template>
 <div>
  <div class="back"></div>
  <div id="abox">
  <div id="qbox">
    <h1 id="qid">Q.{{num}}<span id="numq">{{num}}/12</span></h1>
    <h2 id="titleid">{{ title }}</h2>
  </div>
  <br><br><br><br><br><br>
    <br><br>
      <div id="allbox">
    <div class="a" id="cbtn1">
      <img :src="img1" alt="" id="img1">
    <button  @click="findType(1)"  id="choicebtn">{{ choice1 }}</button >
    </div>
    <div class="a" id="cbtn2">
      <img :src="img2" alt="" id="img2">
    <button  @click="findType(-1)"  id="choicebtn">{{ choice2 }}</button >
      </div>
    </div>
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
    img1: null, 
    im2: null,
    EI: 0,
    NS: 0,
    FT: 0,
    JP: 0,
    result: "",
    genres: []
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
      this.img1 = res.data.picture1
      this.img2 = res.data.picture2
      // console.log(this.title)
    })
    .catch(err => {console.log(err)})
  },
  getResult(){
    if(this.EI > 0){
      this.result = this.result + "E"
      this.genres.push(12, 28) // 모험, 액션
    }
    else{
      this.result = this.result + "I"
      this.genres.push(16, 10751)
    }
    if(this.NS > 0){
      this.result = this.result + "N"
      this.genres.push(14, 10752)
    }
    else{
      this.result = this.result + "S"
      this.genres.push(36, 37, 99)
    }
    if(this.FT > 0){
      this.result = this.result + "F"
      this.genres.push(18, 10402, 10749)
    }
    else{
      this.result = this.result + "T"
      this.genres.push(27, 53)
    }
    if(this.JP > 0){
      this.result = this.result + "J"
      this.genres.push(80, 9648)
    }
    else{
      this.result = this.result + "P"
      this.genres.push(35, 10770)
    }
    const payload = {
      result: this.result,
      genres: this.genres
    }
    // console.log(payload)
    this.$store.commit('GET_MBTI', payload)
  }
 }

}
</script>

<style scoped>
div.back {
  background-color: black;
  z-index: -1;
}

#abox{
  width: 1000px;
}

#qbox{
  width: 700px;
  margin-left: 580px; margin-right: auto;
}

#allbox{
  margin-left: auto; margin-right: auto;
  width: 1800px;
  margin-left: 200px;
  
}



#qid{
  color: white;
  font-size: 75px;
  /* float: left; */
  /* margin-right: 550px; */
  font-weight: bold;
  float: left;
  
}


#numq{
  color: rgb(172, 0, 0);
  font-size: 25px;
  margin-top: 20px;
  margin-left: 10px;
}

#titleid{
  font-style: italic;
  float: left;
  color:white;
  font-weight: bold;
  margin-bottom: 40px;
  /* margin-left: 30px; */
  /* margin-right: 30px; */
  /* font-weight: bold; */
  font-size: 37px;
  /* -webkit-background-clip: text;
  color: transparent;
  text-shadow: -1px 0 lightgrey, 0 1px rgb(28, 27, 27), 1px 0 rgb(94, 85, 85); */
  
}



/* img{
  width: 700px;
  height: 400px;
  border-radius: 30px;
  float: left;
  margin-left: 5px;
} */

#img1{
  width: 700px;
  height: 400px;
  border-radius: 30px;
  float: left;
  margin-left: 5px;
}

#img2{
  width: 700px;
  height: 400px;
  border-radius: 30px;
  float: left;
}

#cbtn1{
  float: left;
  /* margin-left: 250px; */
  width: 760px;
}

#cbtn2{
  float: left;
  /* margin-left: 20px; */
  width: 760px;
}

#choicebtn{
  /* margin: 5px; */
  width: 705px;
  padding: 20px;
  border-radius: 15px;
  /* border: 0.5px solid; */
  font-size: 22px;
  color: black;
  font-weight: bold;
  /* background-color: rgb(23, 22, 22); */
  /* border: solid rgb(23, 22, 22); */
  /* margin-left: auto; margin-right: auto; */
  margin-right: 48px;
  margin-top: 10px;

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
  margin-left: auto; margin-right: auto;
}

.a:hover {
  transform: scale(1.05);
  
}

.a:hover button {
  background-color: red;
  border: solid red;
  color: white;
} 





/* 수정함 */

</style>