<template>
    <form @submit.prevent="createComment">
      <br>
      <div class="col-auto">
      <input type="text" v-model="content" class="form-control" id="inputid" placeholder="감상평을 등록해주세요.">
      </div>
      <div class="col-auto">
      <input type="submit" id="submit" class="btn btn-danger">
      </div>
    </form>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentForm',
  data(){
    return{
      content: null,
    }
  },
  props:{
    movieId: null,
  },
  methods: {
    createComment(){
      const content = this.content
      if (!content){
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/api/movies/${this.movieId}/comments/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          content: content,
        }
      })
      .then(() => {
        this.$emit('update-list')
        this.content = ''
      })
      .catch(err => console.log(err))
    }
  }
}
</script>

<style scoped>
#inputid{
  float: left;
  margin-top: -20px;
  width: 1100px;
  height: 50px;
  
}

#submit{
  float: left;
  /* position: absolute;
  top: 610px;
  left : 470px; */
  height: 46px;
  width: 80px;
  background-color: red;
  margin-top: -20px;
  height: 50px;
  
}



</style>