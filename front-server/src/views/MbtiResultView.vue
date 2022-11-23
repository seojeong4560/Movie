<template>
  <div>
    <br><br><br>
    <h1 id="mbtititle">당신의 MBTI는?</h1>
    <h2 id="mbti">{{ mbti }}</h2>
    <p>{{title}}</p>
    <p>{{sub_title}}</p>
    <p>{{char}}</p>
    <p>{{genres}}</p>
    <img :src="img" alt="">
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MbtiResultView',
  computed:{
    mbti(){
      return this.$store.state.mbti
    }
  },
  created(){
    this.getMbtiDetail()
  },
  data(){
    return {
      title: null,
      sub_title: null,
      char: null,
      genres: null,
      img: null,
    }
  },
  methods:{
    getMbtiDetail(){
      axios({
        method: 'get',
        url: `${API_URL}/api/movies/mbti/detail/${this.mbti}`
      })
      .then(res => {
        this.title = res.data.title
        this.sub_title = res.data.sub_title
        this.char = res.data.char
        this.genres = res.data.genres
        this.img = res.data.img
        // console.log(res)
      })
      .catch(err => { console.log(err) })
    },    
  }
}
</script>

<style scoped>
#mbtititle{
  color: white;
  font-size: 50px;
  font-weight: bold;
  
}

#mbti{
  color: yellow;
  font-size: 50px;
}

/* 수정 */

</style>