<template>
  <div>
    <div class="box-wrap">
      <div class="box">
        <div class="a">
          <img id="mainimg" src="https://t1.daumcdn.net/cfile/tistory/2544DC3C55C17C9005" alt="">
        </div>
        <div class="info">
          <br>
          <h1 id="h1tag">오늘은 이런 영화 어때요?</h1>
          <br><br><br><br>
          <button id="mainbtn" type="button" class="btn btn-danger">Let's go Choose</button>
        </div>
      </div>
    </div>
    <br><br>
    <h2 id="h2word2"></h2>
    <h3 id="mdh3">I</h3>
    <h2 id="h2word">최신 영화</h2>
    <br><br><br>
    <MovieList :movies="latest_movies"/>
    <br><hr><br>
    <h3 id="mdh3">I</h3>
    <h2 id="h2word">평점 높은 영화</h2>
    <br><br><br>
    <MovieList :movies="highscore_movies"/>
    <br><hr><br>
    <h3 id="mdh3">I</h3>
    <h2 id="h2word">인기 영화</h2>
    <br><br><br>
    <MovieList :movies="like_movies"/>
    <br><br>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'

export default {
  name: 'MovieView',
  components:{
    MovieList,
  },
  created(){
    this.getMovieList()
  },
  computed: {
    latest_movies(){
      return this.$store.state.latest_movies
    },
    highscore_movies(){
      return this.$store.state.highscore_movies
    },
    like_movies(){
      return this.$store.state.like_movies
    }
  },
  methods: {
    getMovieList(){
      this.$store.dispatch('getMovieList')
    },
  }

}
</script>

<style scoped>
body {
  background-color: black;
}

#mainimg{
  width: 1100px;
  height: 500px;
}

#h2word{
  color: azure;
  text-align: left;
  margin-left: 15px;
  font-size: 28px;
  margin-bottom: 17px;
  text-shadow: -1px 0 rgb(238, 231, 231), 0 1px rgb(244, 237, 237);
  float: left;

}

#mdh3{
  float: left;
  color: red;
  font-weight: 750;
}

#h2word2{
  color: red;
  float: left;
  margin-left: 10px;
  margin-right: 5px;
  font-size: 35px;
  
}

.a img {
  transition: all 0.5s linear;
}
.a:hover img {
  transform: scale(1.05);
}


.box {
  position: relative;
  /* width: 400px; height: 300px; */
  /* border: 7px solid #283593; */
  box-shadow: 1px 1px 3px rgba(0,0,0,0.4);
}

.box img {
  width: 100%;
  padding: 10px;
}

.box .info {
  color: black;
  /* font-weight: bolder; */
  position: absolute; left: 0%; top: 40%;
  background: rgba(15, 15, 15, 0.555);
  width: 100%;
  height: 320px;
  /* padding: 15px; */
  box-sizing: border-box;
  /* opacity: 0; */
  /* transition: opacity 0.9s ease-in-out; */
  
}

.box:hover .info {
  opacity: 1;
}
/* .box .info h3 {
  font-size: 24px;
  padding-bottom: 0.4em;
  overflow:hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  text-transform: uppercase;
} */

.box .info p {
  font-size: 20px;
  text-overflow: ellipsis;
  white-space: nowrap;
  text-transform: uppercase;
}

#h1tag{
  font-weight:bolder;
  float: left;
  padding-left: 45px;
  /* margin-top: 5px; */
  font-style: italic;
  color: rgb(236, 227, 227);
  font-size: 50px;
}

#mainbtn{
  float: left;
  margin-left: 45px;
  background-color: red;
  width: 200px;
  height: 50px;
  font-size: 20px;
  font-weight: bold;

}


</style>