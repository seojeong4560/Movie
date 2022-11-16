<template>
  <div>
    <h1>MovieView</h1>
    <hr>
    <MovieList :movies="latest_movies"/>
    <MovieList :movies="highscore_movies"/>
    <MovieList :movies="like_movies"/>
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

<style>

</style>