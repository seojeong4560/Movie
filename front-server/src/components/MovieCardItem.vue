<template>
  <div>
    <div class="box-wrap">
      <div class="box">
        <div class="a">
          <div id="imgitem">
            <img :src="movieImgURL" alt="" @click="detail" >
          </div>
          <div class="info2">
            <p id="movietitle">{{ movie.title }}</p>
          </div>
            <div class="info">
            <br><br><br>
            <star-rating :rating="movie.vote_average/2" :read-only="true" :increment="0.01"></star-rating>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'

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
  components: {
    StarRating
  }
}
</script>

<style scoped>
#imgitem{
  float: left;
  /* padding-left: 5px; */
  /* padding-bottom: 50px ; */
  transition: all 0.4s linear;
  width: 315px;
  height: 330px;
  
}

.a{
  /* width: 300px; */
  /* margin: 0px auto; */
}

.a:hover img{
  transform: scale(1.1, 1.1);
  filter: brightness(20%);
  transition: all 0.8s linear;
}

.box-wrap {
  display: flex;
  float: left;
}

.box {
  position: relative;
  width: 330px; height: 310px;
  /* border: 7px solid #283593; */
  box-shadow: 1px 1px 3px rgba(0,0,0,0.4);
  padding-left: 15px;
  margin-bottom: 80px;
}

.box img {
  width: 100%;
  /* padding: 5px; */
}



.box .info {
  color: #fff;
  position: absolute; left: 12%; top: 55%;
  /* background: rgba(0,0,0,0.5); */
  width: 100%;
  height: 200px;
  /* padding: 15px; */
  box-sizing: border-box;
  opacity: 0;
  transition: opacity 0.35s ease-in-out;
  
}

.box:hover .info {
  opacity: 1;
}


.box .info p {
  font-size: 20px;
  text-overflow: ellipsis;
  white-space: nowrap;
  text-transform: uppercase;
}

.box .info2 {
  /* color: black; */
  /* font-weight: bolder; */
  position: absolute; left: 0%; top: 85%;
  /* background: rgba(15, 15, 15, 0.555); */
  width: 100%;
  height: 320px;
  /* padding: 15px; */
  box-sizing: border-box;
  /* opacity: 0; */
  /* transition: opacity 0.9s ease-in-out; */
  transition: top 0.9s;
  
}

.box:hover .info2 {
  opacity: 1;
  top: 170px;

}

.box .info2 p {
  font-size: 23px;
  text-overflow: ellipsis;
  white-space: nowrap;
  text-transform: uppercase;
}

#movietitle{
  font-style: italic;
  /* color: lightgrey; */
  font-weight: 900;
  /* font-family: 'Staatliches', cursive; */
  font-size: 1.2em;
  text-align: center;
  /* color: BABAC1; */
  margin: 0;
  /* background-image: linear-gradient(90deg, red, orange, yellow, purple); */
  -webkit-background-clip: text;
  color: transparent;
  text-shadow: -1px 0 lightgrey, 0 1px rgb(28, 27, 27), 1px 0 rgb(94, 85, 85);
  width: 300px;
  margin-left: auto; 
  margin-right: auto;
}


body {
  font-family: 'Raleway', sans-serif;
}

.custom-text {
  font-weight: bold;
  font-size: 1.9em;
  border: 1px solid #cfcfcf;
  padding-left: 10px;
  padding-right: 10px;
  border-radius: 5px;
  color: #999;
  background: #fff;

}

#starrating{
  padding-left: 39px;
  padding-top: 5px;
  margin-left: auto; 
  margin-right: auto;
  
}

</style>