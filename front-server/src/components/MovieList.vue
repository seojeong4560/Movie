<template>
  <div>
    <h2>MovieList</h2>
    <hr>
    <MovieListItem
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem'

export default {
  name: 'MovieList',
  components:{
    MovieListItem,
  },
  props:{
    movies: Array,
  },
  computed: {
  }
}
</script>

<style>

</style>