<template>
  <swiper ref="filterSwiper" :options="swiperOption" role="tablist">
  <!-- <div class="box-wrapper"> -->
    <hr>
      <MovieListItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      />
  <!-- </div> -->
  </swiper>
</template>

<script>
import MovieListItem from '@/components/MovieListItem'

import 'swiper/dist/css/swiper.css'
import { swiper } from 'vue-awesome-swiper'

export default {
  name: 'MovieList',
  data () {
    return {
      swiperOption: {
        slidesPerView: 'auto',
        spaceBetween: 6, // swiper-slide 사이의 간격 지정
        slidesOffsetBefore: 0, // slidesOffsetBefore는 첫번째 슬라이드의 시작점에 대한 변경할 때 사용
        slidesOffsetAfter: 0, // slidesOffsetAfter는 마지막 슬라이드 시작점 + 마지막 슬라이드 너비에 해당하는 위치의 변경이 필요할 때 사용
        freeMode: true, // freeMode를 사용시 스크롤하는 느낌으로 구현 가능
        centerInsufficientSlides: true, // 컨텐츠의 수량에 따라 중앙정렬 여부를 결정함
      }
    }
  },
  components:{
    MovieListItem,
    swiper,
  },
  props:{
    movies: Array,
  },
  computed: {
  }
}
</script>

<!--<style>
/* .box-wrapper {
  display: flex;
  width: 100;
} */

</style>-->

<style lang="scss" scoped>
.swiper-container {
  .swiper-wrapper {
    .swiper-slide {
      width: auto; // auto 값을 지정해야 슬라이드의 width값이 텍스트 길이 기준으로 바뀜
      min-width: 56px; // min-width를 지정하지 않을 경우 텍스트가 1개 내지는 2개가 들어갈 때 탭 모양이 상이할 수 있으므로 넣어준다.
      // padding: 0px 14px;
      font-size: 14px;
      // line-height: 36px;
      // text-align: center;
      // color: #84868c;
      // border: 0;
      // border-radius: 18px;
      // background: #f3f4f7;
      // appearance: none;
      // cursor: pointer;
    }
  }
}
</style>

