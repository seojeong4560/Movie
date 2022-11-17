<template>
  <div>
    <img :src="movieImgURL" alt="" @click="detail">
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
  },
  methods: {
    detail(){
      // console.log(this.movie.id)
      return this.$router.push({name: 'DetailView', params: { id: this.movie.id } })
    }
  },
}
</script>

<style>

</style>