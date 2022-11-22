<template>
  <div>
    <h2>{{ title }}</h2>
    <p @click="findType(1)">{{ choice1 }}</p>
    <p @click="findType(-1)">{{ choice2 }}</p>
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

<style>

</style>