<template>
  <div>
    <div class="back"></div>
    <br>
      <div id="MVDetail">
      <div id="mvbox">
      <img :src="movieImgURL" alt="" id="movieImage">
      <h3 id="movieTitle">{{movie.title}}</h3>
      <p id="genre">
        Genre: 
        <span v-for="genre in genres" :key="genre.id">
          {{ genre.name }} 
        </span>
      </p>
      <p id="overview">{{movie.overview}}</p>
      <star-rating :increment="0.01" :fixed-points="2" id="star"></star-rating>
      <br>
        <button id="btn1" type="button" class="btn btn-danger">Play</button>
        <button id="btn3" type="button" class="btn btn-light"><img id="img1" src="https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.0/72x72/2764.png" alt=""></button> 
        <button id="btn2" type="button" class="btn btn-light">+</button> 
    </div>
        <div id="commentForm">
          <CommentForm 
            :movie-id = "movieId"
            @update-list="getMovieDetail"
          />
          <CommentList :comments="commentSet"/>
        </div>
    </div>
    
    <div id="movieList">
      <hr id = "hr">
      <h2 id="h2word">관련 영화</h2>
      <MovieList :movies="sameGenres"/>
    </div>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
import axios from 'axios'
import MovieList from '@/components/MovieList'
import CommentList from '@/components/CommentList'
import CommentForm from '@/components/CommentForm'


const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  data(){
    return {
      movie: Object,
      sameGenres: [],
      movieId: this.$route.params.id,
      commentSet: [],
    }
  },
  components:{
    MovieList,
    StarRating,
    CommentList,
    CommentForm,
  },
  created(){
    this.getMovieDetail()
  },
  computed: {
    movieImgURL(){
      return `https://themoviedb.org/t/p/w600_and_h900_bestv2${this.movie.poster_path}`
    },
    genres(){
      return this.movie.genres
    }
  },
  methods: {
    getMovieDetail(){
      axios({
        method: 'get',
        url: `${API_URL}/api/movies/detail/${this.movieId}`
      })
      .then(res => {
        this.movie = res.data.movie
        this.sameGenres = res.data.same_genres
        this.commentSet = res.data.movie.comment_set
        // console.log(res)
      })
      .catch(err => { console.log(err) })
    },
  },
  
  
}
</script>

<style scoped>


#movieImage{
  width: 270px;
  float: left;
  margin-left: 30px;
  margin-right: 20px;
  margin-bottom: 20px;
}

#MVDetail{
  padding-top: 50px;
  text-align: left;
  /* margin-right: 25px; */
  
}

#movieTitle{
  color: azure;
  font-size: 40px;
  font-weight: bold;
  
  
}

#genre{
  color: #babac1;
  font-size: 20px;
  font-weight: bold;
  white-space: normal;
}

#overview{
  color: #babac1;
  white-space: normal;
} 

#hr{
  color: #babac1;
  height: 15px;
}

#btn1{
  width: 100px;
  height: 45px;
  margin-bottom: 80px;
}

#btn2{
  margin-left: 5px;
  width: 50px;
  height: 45px;
  margin-bottom: 80px;
}

#btn3{
  margin-left: 5px;
  width: 60px;
  height: 45px;
  margin-bottom: 80px;
}

#img1{
  width: 35px;
  height: 35px;
}

#movieList{
  margin-top: 100px;
  
  
}

#h2word{
  color: azure;
  text-align: left;
  margin-left: 15px;
  font-size: 28px;
}

body {
  font-family: 'Raleway', sans-serif;
}

.custom-text {
  font-weight: bold;
  font-size: 1.9em;
  border: 1px solid #cfcfcf;
  padding-left: 10px;
  padding-right: 10px;
  border-radius: 5px;
  color: #999;
  background: #fff;
  
}

#commentForm{
  /* float: left; */
  padding-left: 30px;
  padding-top: 20px;
  
}

#commentForm{
  background-color: rgb(16, 15, 15);
  width: 650px;
  border-radius: 20px;
  height: 380px;
  margin-left: 15px;
  /* float: right; */
  /* margin-right: 10px; */
  position: absolute;
  right: 10px;
  top: 190px
  
  
}

#mvbox{
  width: 1200px;
}

#star{
  width: 100px;
}

/* 수정 */

</style>