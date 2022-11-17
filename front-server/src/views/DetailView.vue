<template>
  <div>
    <h1>Detail</h1>
    <div>
       <img :src="movieImgURL" alt="">
       <h3>{{movie.title}}</h3>
       <p>
        Genre: 
        <span v-for="genre in genres" :key="genre.id">
          {{ genre.name }} 
        </span>
       </p>
       <p>{{movie.overview}}</p>
    </div>
    <MovieList :movies="same_genres"/>
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
      same_genres: Array,
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
        url: `${API_URL}/api/movies/detail/${this.$route.params.id}`
      })
      .then(res => {
        // console.log(res)
        this.movie = res.data.movie
        this.same_genres = res.data.same_genres
      })
      .catch(err => { console.log(err) })
    }
  }
}
</script>

<style>

</style>