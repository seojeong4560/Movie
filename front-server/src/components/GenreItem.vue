<template>
  <div>
    <input type="checkbox" :id="genre.id" :value="genre.id" v-model="checked"  >
    <label for="a" >{{genre.name}}</label>
    <br><br>
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

<style scoped>
/* input{
  float: left;
  width: 35px;
  height: 35px;
} */

label{
  float: left;
  color: #ECE3E3;
  margin-left: 13px;
  font-size: 27px;
  font-weight: bold;
}

input[type="checkbox"] {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  background: #ECE3E3;
  border-radius: 4px;
  cursor: pointer;
  height: 16px;
  outline: 0;
  width: 16px;
  float: left;
  width: 35px;
  height: 35px;
  border-radius: 7px;
}


input[type="checkbox"]::after {
  border: solid #fff;
  border-width: 0 2px 2px 0;
  content: '';
  display: none;
  height: 40%;
  left: 40%;
  position: relative;
  top: 20%;
  transform: rotate(45deg);
  width: 15%;
  float: left;
  
}


input[type="checkbox"]:checked {
  background: red;
  border-radius: 10px;
}


input[type="checkbox"]:checked::after {
  display: block;
}



/* 수정 */

</style>