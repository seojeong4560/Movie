<template>
  <div>
    <br>
      <img :src="movieImgURL" alt="" id="movieImage">
      <div id="MVDetail">
      <h3 id="movieTitle">{{movie.title}}</h3>
      <p id="genre">
        Genre: 
        <span v-for="genre in genres" :key="genre.id">
          {{ genre.name }} 
        </span>
      </p>
      <p id="overview">{{movie.overview}}</p>
      <button id="btn1" type="button" class="btn btn-danger">Play</button>
      <button id="btn3" type="button" class="btn btn-light"><img id="img1" src="https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.0/72x72/2764.png" alt=""></button> 
      <button id="btn2" type="button" class="btn btn-light">+</button> 
    </div>
    <div id="movieList">
      <hr id = "hr">
    <MovieList :movies="same_genres"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieList from '@/components/MovieList'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  data(){
    return {
      movie: Object,
      same_genres: [],
      movieId: this.$route.params.id
    }
  },
  components:{
    MovieList,
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
        // console.log(res)
        this.movie = res.data.movie
        this.same_genres = res.data.same_genres
      })
      .catch(err => { console.log(err) })
    }
  },

}
</script>

<style>
#movieImage{
  width: 270px;
  float: left;
  margin-left: 30px;
  margin-right: 20px;
}

#MVDetail{
  padding-top: 100px;
  text-align: left;
  margin-right: 25px;
  
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
}

#btn2{
  margin-left: 5px;
  width: 50px;
  height: 45px;
}

#btn3{
  margin-left: 5px;
  width: 60px;
  height: 45px;
}

#img1{
  width: 35px;
  height: 35px;
}

#movieList{
  margin-top: 100px;
  
  
}
</style>