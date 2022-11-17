<template>
  <div>
    <img :src="movieImgURL" alt="">
    <p>{{movie.title}}</p>
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  props:{
    movie: Object,
  },
  computed: {
    movieImgURL(){
      return `https://themoviedb.org/t/p/w600_and_h900_bestv2${this.movie.poster_path}`
    },
  }
}
</script>

<style>

</style>