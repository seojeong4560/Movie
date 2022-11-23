<template>
  <div>
    <br><br><br>
    <div id="genrebox">
    <div class="container">
    <GenreItem
      v-for="genre in genres"
      :key="genre.id"
      :genre="genre"
    />
    </div>
    </div>
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

<style scoped>
/* #genrebox{
  background-color: rgb(16, 15, 15);
  padding: 20px;
  width: 500px;
  height: 950px;
  margin-left: 50px;
  border-radius: 20px;
} */

.container {
  overflow: auto;
  float: left;
  margin-top: -45px;
  border-radius: 20px;
  width: 580px;
  height: 700px;
  background-color: rgb(16, 15, 15);
  padding: 40px;
  margin-left: 50px;
}

.container::-webkit-scrollbar {
    width: 10px;
  }

.container::-webkit-scrollbar-thumb {
    background-color: red;
    border-radius: 10px;
    
  }


.container::-webkit-scrollbar-track {
    background-color: black;
    border-radius: 10px;
    box-shadow: inset 0px 0px px grey;
  }


img{
  float: right;
  padding-right: 50px;
  margin-top: 400px;
  width: 600px;
}

/* 수정 */

</style>