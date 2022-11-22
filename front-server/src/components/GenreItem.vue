<template>
  <div>
    <input type="checkbox" :id="genre.id" :value="genre.id" v-model="checked">
    <label for="a">{{genre.name}}</label>
    <br>
  </div>
</template>

<script>
export default {
  name: 'GenreItem',
  data(){
    return{
      checked: null,
    }
  },
  props:{
    genre: Object,
  }

}
</script>

<style>

</style>