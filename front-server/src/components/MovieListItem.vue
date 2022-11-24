<template>
<swiper-slide role="tab">
  <div class="box-wrap">
    <div class="box">
      <div class="a">
        <img :src="movieImgURL" alt="" @click="detail">  
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
  </swiper-slide>
</template>

<script>
import StarRating from 'vue-star-rating'
import { swiperSlide } from 'vue-awesome-swiper'


export default {
  name: 'MovieListItem',
  data() {
    return {
      ratings: null,
    }
  },
  props:{
    movie: Object,
  },
  computed: {
    movieImgURL(){
      return `https://themoviedb.org/t/p/original${this.movie.backdrop_path}`
    },
  },
  methods: {
    detail(){
      return this.$router.push({name: 'DetailView', params: { id: this.movie.id } })
    }
  },
  components: {
    swiperSlide,
    StarRating
  }
}
</script>

<style scoped>
img{
  /* max-width: 100%; */
  transition: all 0.4s linear;
  width: 250px;
  height: 320px;
  padding: 5px;
}

.a{
  width: 300px;
  margin: 0px auto;
}

.a:hover img{
  transform: scale(1.1, 1.1);
  filter: brightness(20%);
}

/* .box-wrap {
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center
} */
.box {
  position: relative;
  /* width: 400px; height: 300px; */
  /* border: 7px solid #283593; */
  box-shadow: 1px 1px 3px rgba(0,0,0,0.4);
}

.box img {
  width: 100%;
  padding: 5px; 
}



.box .info {
  color: #fff;
  position: absolute; left: 0; top: 45%;
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
/* .box .info h3 {
  font-size: 24px;
  padding-bottom: 0.4em;
  overflow:hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  text-transform: uppercase;
} */

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
  font-size: 1.7em;
  text-align: center;
  /* color: BABAC1; */
  margin: 0;
  /* background-image: linear-gradient(90deg, red, orange, yellow, purple); */
  -webkit-background-clip: text;
  color: transparent;
  text-shadow: -1px 0 lightgrey, 0 1px rgb(28, 27, 27), 1px 0 rgb(94, 85, 85);
}


/* #movietitle2{
  font-style: italic;
  color: lightgrey;
  font-weight: bolder;
} */

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
}



</style>