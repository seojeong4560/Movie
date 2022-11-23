<template>
  <div>
    <br><br>
    <div id="checkboxlist">
    <span 
      v-for="genre in genres"
      :key="genre.id"
    >
      <input type="checkbox" v-model="checked" :value="genre.id" :id="genre.id">
      <label :for="genre.id" id="genrename">{{ genre.name }}</label>      
    </span>
    <button @click="getRecommend">push</button>
    <!-- <p>checked</p>
    <p>{{checked}}</p> -->
    </div>
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
  margin-top: 30px;
  border-radius: 20px;
  width: 2300px;
  height: 600px;
  background-color: rgb(16, 15, 15);
  padding: 40px;
  margin-left: 250px;
}



#checkboxlist{
  background-color: rgb(38, 35, 35);
  width: 800px;
  /* margin-left: 200px; */
  color: white;
  border-radius: 10px;
  margin-left: auto;
  margin-right: auto;
  
}

input{
  margin-left: 20px;
  margin-top: 20px;
}

#genrename{
  font-size: 25px;
}

input[type="checkbox"] {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  background: #fff;
  border-radius: 4px;
  cursor: pointer;
  height: 16px;
  outline: 0;
  width: 25px;
  height: 25px;
}
input[type="checkbox"]::after {
  border: solid #fff;
  border-width: 0 2px 2px 0;
  content: '';
  display: none;
  height: 40%;
  left: 40%;
  position: relative;
  top: 20%;
  transform: rotate(45deg);
  width: 15%;
}
input[type="checkbox"]:checked {
  background: #505bf0;
}
input[type="checkbox"]:checked::after {
  display: block;
}

/* 수정 */

</style>