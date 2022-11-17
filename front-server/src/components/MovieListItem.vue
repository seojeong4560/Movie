<template>
  <div>
    <swiper-slide role="tab">
      <div id="card">
        <img :src="movieImgURL" alt="">
        <p>{{movie.title}}</p>
      </div>
    </swiper-slide>
  </div>
</template>

<script>
import 'swiper/dist/css/swiper.css'
import { swiperSlide } from 'vue-awesome-swiper'

export default {
  name: 'MovieListItem',
  props:{
    movie: Object,
  },
  computed: {
    movieImgURL(){
      return `https://themoviedb.org/t/p/w300_and_h300_bestv2${this.movie.poster_path}`
    },
  },
  components: {
    swiperSlide
  }
}
</script>

<style >
.swiper-slide {
      width: auto; 
      min-width: 56px; 
      padding: 0px 14px;
      font-size: 20px;
      line-height: 36px;
      text-align: center;
      color: hotpink;
      border: 0;
      border-radius: 18px;
      background: black;
      appearance: none;
      cursor: pointer;
    }
/* #card {
  width : 100px;
} */

</style>