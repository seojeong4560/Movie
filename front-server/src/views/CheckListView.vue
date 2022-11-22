<template>
  <div>
    <GenreItem
      v-for="genre in genres"
      :key="genre.id"
      :genre="genre"
    />
    <br>
    <!-- <span>체크 한 값 : {{ checkedNames }}</span> -->
  </div>
</template>

<script>
import GenreItem from '@/components/GenreItem'

export default {
  name: 'CheckListView',
  // data(){
  //   return{
  //     checkedNames: [],
  //   }
  // },
  components:{
    GenreItem,
  },
  computed: {
    genres(){
      return this.$store.state.genres
    }
  },
  created(){
    this.getGenreList()
  },
  methods: {
    getGenreList(){
      this.$store.dispatch('getGenreList')
    }
  }


}
</script>

<style>

</style>