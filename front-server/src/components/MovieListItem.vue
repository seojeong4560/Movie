<template>
  <div>
    <p>{{movie.title}}</p>
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  props:{
    movie: Object,
  }
}
</script>

<style>

</style>