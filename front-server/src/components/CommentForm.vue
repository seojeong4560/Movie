<template>
  <div>
    <h4>댓글 작성</h4>
    <form @submit.prevent="createComment">
      <input type="text" v-model="content">
      <input type="submit" id="submit">
    </form>
  </div>
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

<style>

</style>