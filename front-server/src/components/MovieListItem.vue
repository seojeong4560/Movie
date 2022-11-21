<template>
<swiper-slide role="tab">
  <div class="box-wrap">
    <div class="box">
      <div class="a">
        <img :src="movieImgURL" alt="" @click="detail">  
      </div>
      <div class="info">
        <br>
        <p id="movietitle">{{ movie.title }}</p>
        <div class="star-rating space-x-4 mx-auto">
          <input type="radio" id="5-stars" name="rating" value="5" v-model="ratings"/>
          <label for="5-stars" class="star pr-4">★</label>
          <input type="radio" id="4-stars" name="rating" value="4" v-model="ratings"/>
          <label for="4-stars" class="star">★</label>
          <input type="radio" id="3-stars" name="rating" value="3" v-model="ratings"/>
          <label for="3-stars" class="star">★</label>
          <input type="radio" id="2-stars" name="rating" value="2" v-model="ratings"/>
          <label for="2-stars" class="star">★</label>
          <input type="radio" id="1-star" name="rating" value="1" v-model="ratings" />
          <label for="1-star" class="star">★</label>
        </div>
      </div>
    </div>
  </div>
  </swiper-slide>
</template>

<script>
import {swiperSlide } from 'vue-awesome-swiper'


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
      return `https://themoviedb.org/t/p/w300_and_h300_bestv2${this.movie.poster_path}`
    },
  },
  methods: {
    detail(){
      return this.$router.push({name: 'DetailView', params: { id: this.movie.id } })
    }
  },
  components: {
    swiperSlide
  }
}
</script>

<style scoped>
img{
  /* max-width: 100%; */
  transition: all 0.5s linear;
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
  background: rgba(0,0,0,0.5);
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

#movietitle{
  font-style: italic;
  color: lightgrey;
  font-weight: bolder;
  
  
}

.star-rating {
  display: flex;
  flex-direction: row-reverse;
  font-size: 2.25rem;
  line-height: 2.5rem;
  justify-content: space-around;
  padding: 0 0.2em;
  text-align: center;
  width: 5em;
}
 
.star-rating input {
  display: none;
}
 
.star-rating label {
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 0.3px;
  -webkit-text-stroke-color: #fff58c;
  cursor: pointer;
}
 
.star-rating :checked ~ label {
  -webkit-text-fill-color: gold;
}
 
.star-rating label:hover,
.star-rating label:hover ~ label {
  -webkit-text-fill-color: gold
}

</style>