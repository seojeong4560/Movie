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
    <!-- <p>checked</p>
    <p>{{checked}}</p> -->
    </div>
    <div class="a">
    <button @click="getRecommend" class="btn btn-danger" id="push">{{this.$store.state.username}}님을 위한 추천 받기</button>
    </div>
    <br>
    <br><hr id="hr"><br>
    <h2 v-if="recommended" id="recotitle">{{this.$store.state.username}}님 오늘은 이런 영화 어떠세요? </h2>
    <br><br><br>
    <div id="mvcardall">
    <MovieCardList :movies="recommended"/>
    </div>
    <br><br>
  </div>
</template>

<script>
import axios from 'axios'
import MovieCardList from '@/components/MovieCardList'

const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'CheckListView',
  components:{
    MovieCardList,
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

.a button {
  transition: all 0.6s linear;
}
.a:hover button {
  transform: scale(1.05);
}


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
  background-color: rgb(25, 23, 23);
  width: 900px;
  /* margin-left: 200px; */
  color: white;
  border-radius: 10px;
  margin-left: auto;
  margin-right: auto;
  
}

input{
  margin-left: 20px;
  margin-top: 20px;
  margin-right: 10px;
  
}

#genrename{
  font-size: 25px;
  /* font-weight: bold; */

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
  background: red;
  border-radius: 5px;
}
input[type="checkbox"]:checked::after {
  display: block;
}

#hr{
  color: #babac1;
  height: 15px;
}

#recotitle{
  color: azure;
  /* font-weight: bold; */
  font-size: 35px;
}

#push{
  background-color: red;
  margin-left: 10px;
  margin-bottom: 10px;
  width: 430px;
  height: 57px;
  font-size: 20px;
  font-weight: bold;
  margin-top: 8px;
  border-radius: 60px ;
}

#mvcardall{
  margin-left: 100px; 
  margin-right: auto;
}

/* 수정 */

</style>