<template>
  <div>
    <MovieCardItem
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script>
import MovieCardItem from '@/components/MovieCardItem'
export default {
  name: 'MovieCardList',
  components:{
    MovieCardItem,
  },
  props:{
    movies: Array,
  }

}
</script>

<style>

</style>