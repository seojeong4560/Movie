<template>
  <div>
    <span
      v-for="genre in genres"
      :key="genre.id"
    >
      <input type="checkbox" v-model="checked" :value="genre.id" :id="genre.id">
      <label :for="genre.id">{{ genre.name }}</label>      
    </span>
    <!-- <p>checked</p>
    <p>{{checked}}</p> -->
    <button @click="getRecommend">push</button>
    <br><hr><br>
    <h2>추천 영화</h2>
    <br><br><br>
    <MovieList :movies="recommended"/>
    <br><br>


  </div>
</template>

<script>
import axios from 'axios'
import MovieList from '@/components/MovieList'

const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'CheckListView',
  components:{
    MovieList,
  },
  data(){
    return{
      checked: [],
      recommended: [],
    }
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
    },
    getRecommend(){
      axios({
        method: 'post',
        url: `${API_URL}/api/movies/recommend/`,
        data:{
          genres: this.checked
        }
      })
      .then(res =>{
        // console.log(this.checked)
        // console.log(res)
        this.recommended = res.data.selected_genre
      })
      .catch(err => { console.log(err) })
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