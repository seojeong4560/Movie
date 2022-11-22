<template>
  <div>
    <h1>당신의 MBTI는?</h1>
    <h2>{{ mbti }}</h2>
  </div>
</template>

<script>
export default {
  name: 'MbtiResultView',
  computed:{
    mbti(){
      return this.$store.state.mbti
    }
  }
}
</script>

<style>

</style>