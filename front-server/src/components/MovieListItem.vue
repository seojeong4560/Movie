<template>
  <div>
    <img :src="movieImgURL" alt="" @click="detail">
    <p>{{movie.title}}</p>
    <router-link :to="{name: 'DetailView', params: { id: movie.id} }">[Detail]</router-link>
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
      return this.$router.push({name: 'DetailView', params: { id: this.movie.id } })
    }
  }
}
</script>

<style>

</style>