<template>
  <div>
    <span
      v-for="genre in genres"
      :key="genre.id"
    >
      <input type="checkbox" v-model="checked" :value="genre.id" :id="genre.id">
      <label :for="genre.id">{{ genre.name }}</label>      
    </span>
    <p>checked</p>
    <p>{{checked}}</p>
  </div>
</template>

<script>
export default {
  name: 'CheckListView',
  data(){
    return{
      checked: [],
    }
  },
  components:{
    // CheckItem,
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

.container::-webkit-scrollbar {
    width: 10px;
  }

.container::-webkit-scrollbar-thumb {
    background-color: red;
    border-radius: 10px;
    
  }


.container::-webkit-scrollbar-track {
    background-color: black;
    border-radius: 10px;
    box-shadow: inset 0px 0px px grey;
  }


img{
  float: right;
  padding-right: 50px;
  margin-top: 400px;
  width: 600px;
}

/* 수정 */

</style>