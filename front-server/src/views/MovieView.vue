<template>
  <div>
    <!-- <div class="back"></div> -->
    <div id="boxwrap" class="box-wrap" :style="`background-image: url(${this.$store.state.randomMovie}); background-size: cover; background-position: center;`">
      <div class="box">
        <!-- <div class="a">
          <img id="mainimg" :src="this.$store.state.randomMovie" alt="" style="background-repeat: no-repeat;">
        </div> -->
        <div class="info" style="background-size: cover; background-position: center;">
          <br>
          <h1 id="h1tag">오늘은 이런 영화 어때요?</h1>
          <br><br><br><br>
          <div class="a">
          <button id="mainbtn" type="button" class="btn btn-danger" @click="checkList">Let's go Choose</button>
          </div>
        </div>
        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
      </div>
    </div>
    <br><br>
    <div v-if="this.$store.state.mbti">
      <h3 id="mdh3">I</h3>
      <h2 id="h2word">{{this.$store.state.mbti_title}} {{this.$store.state.username}}님에게 추천하는 영화</h2>
      <br><br><br>
      <MovieList :movies="mbti_movies"/>
      <br><hr><br>
    </div>
    <div v-if="!this.$store.state.mbti" >
      <p>아직 MBTI를 통한 영화를 추천받지 못하였네요</p>
      <button @click="mbti">mbti로 영화추천받기</button>
    </div>
    <h3 id="mdh3">I</h3>
    <h2 id="h2word">최신 개봉 영화</h2>
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
    <br><hr><br>
    <h3 id="mdh3">I</h3>
    <h2 id="h2word">개봉 예정작</h2>
    <br><br><br>
    <MovieList :movies="upcomming_movies"/>
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
    this.getMovieList(),
    this.randomMovie()
  },
  computed: {
    upcomming_movies(){
      return this.$store.state.upcomming_movies
    },
    latest_movies(){
      return this.$store.state.latest_movies
    },
    highscore_movies(){
      return this.$store.state.highscore_movies
    },
    like_movies(){
      return this.$store.state.like_movies
    },
    mbti_movies(){
      return this.$store.state.mbti_movies
    }
  },
  methods: {
    getMovieList(){
      this.$store.dispatch('getMovieList')
    },
    checkList(){
      return this.$router.push({name: 'CheckListView'})
    },
    randomMovie(){
      return this.$store.commit('RANDOM_MOVIE_PICK')
    },
    mbti(){
      return this.$router.push({name: 'MbtiView'})
    }
  }

}
</script>

<style scoped>
body {
  background-color: black;
}

#boxwrap{
  height: 750px;
}

#mainimg{
  width: 1894px;
  height: 750px;
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

/* .a img {
  transition: all 0.5s linear;
}
.a:hover img {
  transform: scale(1.05);
} */




/* .box {
  position: relative;
  box-shadow: 1px 1px 3px rgba(0,0,0,0.4);
} */

/* .box img {
  width: 100%;
  
} */

.box .info {
  color: black;
  position: absolute; left: 0%; top: 50%;
  background: rgba(15, 15, 15, 0.555);
  width: 100%;
  height: 440px;
  box-sizing: border-box;

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
  /* background-color: red; */
  width: 200px;
  height: 50px;
  font-size: 20px;
  font-weight: bold;

}

.a button{
  transition: all 0.3s linear;
}

.a:hover button {
  transform: scale(1.1);
}


</style>