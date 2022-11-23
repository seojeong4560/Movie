<template>
  <div>
    <br><br><br>
    <h1 id="mbtititle">당신의 영화 MBTI는?</h1>
    <h2 id="mbti">{{ mbti }}</h2>
    <p>{{context}}</p>
  </div>
</template>

<script>
export default {
  name: 'MbtiResultView',
  computed:{
    mbti(){
      return this.$store.state.mbti
    }
  },
  data(){
    return {
      context: null,
    }
  },
  methods:{
    mbti_detail(){
      if(this.mbti == "ISTJ"){
        this.context = "당신의 영화 MBTI는 진지한 모범생형 캐릭터인 ISTJ입니다. 한 번 시작한 일은 끝까지 해내는 유형으로서 주인공으로도 사용되고 조력자 역할인 경우가 많습니다."
      }
      else{
        this.context = "else"
      }
    }
  }
}
</script>

<style scoped>
#mbtititle{
  color: white;
  font-size: 50px;
  font-weight: bold;
  
}

#mbti{
  color: yellow;
  font-size: 50px;
}

/* 수정 */

</style>