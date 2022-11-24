<template>
  <div>
    <br>
    <div id="mbtibox">
    <h1 id="mbtititle">당신의 영화 MBTI는?</h1>
    <h2 id="mbti">{{ mbti }}</h2>
    <br>
    <img :src="img" alt="">
    <br><br>
    <p id="title">"{{title}}"</p>
    </div>
    <br><br><br>
    <div id="resultbox">
    <h1 id="h1tag">당신은</h1>
    <br><br><br><br>
    <p id="sub_title">{{sub_title}}</p>
    <h1 id="h1tag">당신과 같은 MBTI 캐릭터는</h1>
    <br><br><br><br><br>
    <p id="char">{{char}}</p>
    <h1 id="h1tag">당신에게 아래 장르를 추천드려요.</h1>
    <br><br><br><br><br><br>
    <p id="genres">{{genres}}</p>
    <br><br><br><br>
    <MovieList :movies="recommended"/>
    </div>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MbtiResultView',
  components:{
    MovieList,
  },
  computed:{
    mbti(){
      return this.$store.state.mbti
    },
    mbti_genres(){
      return this.$store.state.mbti_genres
    }
  },
  created(){
    this.getMbtiDetail()
    this.getRecommend()
  },
  data(){
    return {
      title: null,
      sub_title: null,
      char: null,
      genres: null,
      img: null,
      recommended: null,
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
  getRecommend(){
      axios({
        method: 'post',
        url: `${API_URL}/api/movies/recommend/`,
        data:{
          genres: this.mbti_genres
        }
      })
      .then(res =>{
        this.recommended = res.data.selected_genre
        const payload = {
          recommended: this.recommended,
          mbti_title: this.title
        }
        this.$store.commit('GET_MBTI_MOVIES', payload)
        // console.log(this.recommended)
      })
      .catch(err => { console.log(err) })
    }
  },
}
</script>

<style scoped>
#mbtititle{
  color: white;
  font-size: 40px;
  font-weight: bold;
  
}

#mbti{
  color: skyblue;
  font-size: 60px;
}

img{
  border-radius: 70%;
  width: 390px;
  height: 350px;
  /* border:3px solid white; */
}

#title{
  color: white;
  font-size: 30px;
  font-weight: bold;
  font-style: italic;

}

#sub_title{
  color: white;
  font-size: 20px;
  /* font-weight: bold; */
  /* font-style: italic; */
  float: left;
  padding-left: 60px;
  font-weight: bold;
  padding-right: 60px;
}

#char{
  color: white;
  font-size: 20px;
  /* font-weight: bold; */
  /* font-style: italic; */
  float: left;
  padding-left: 60px;
  font-weight: bold;
}

#genres{
  color: white;
  font-size: 20px;
  /* font-weight: bold; */
  /* font-style: italic; */
  float: left;
  padding-left: 60px;
  font-weight: bold;
}

#mbtibox{
  float: left;
  padding-left: 100px;
  padding-top: 20px;
}


#resultbox{
  float: left;
  margin-left: 100px;
  padding-top: 40px;
  /* border:3px solid white; */
  width: 1100px;
  border-radius:70px;
  background-color: #100F0F;
}

#h1tag{
  float: left;
  padding-left: 60px;
  font-style: italic;
  font-weight: bold;
  margin-top: 25px;
  color: white;
  
}




/* 수정 */

</style>