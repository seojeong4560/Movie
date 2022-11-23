<template>
  <div>
    <img :src="movieImgURL" alt="" @click="detail">
  </div>
</template>

<script>
export default {
  name: 'MovieCardItem',
  props:{
      movie: Object,
  },
  computed: {
    movieImgURL(){
      return `https://themoviedb.org/t/p/w300_and_h300_bestv2${this.movie.poster_path}`
    },
  },
  methods: {
    detail(){
      return this.$router.push({name: 'DetailView', params: { id: this.movie.id } })
    }
  },
}
</script>

<style>

</style>