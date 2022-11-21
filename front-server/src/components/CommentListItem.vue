<template>
  <div>
    <p>{{ comment.username}}</p>
    <p>{{ comment.content }}</p>
    <p>{{ comment.created_at }}</p>
    <!-- <p @click="updateComment">수정</p> -->
    <button @click="deleteComment">x</button>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentListItem',
  props:{
    comment: Object,
  },
  methods:{
    // updateComment(){
    //   axios({
    //     method: 'put',
    //     url: `${API_URL}/api/movies/comments/${this.comment.id}/`,
    //     data: {
    //       content: content,
    //     }
    //   })
    // },
    deleteComment(){
      axios({
        method: 'delete',
        url: `${API_URL}/api/movies/comments/${this.comment.id}/`,
      })
      .then(() =>{
        this.commit('UPDATE_COMMENTS')
      })
    }
  }
}
</script>

<style>

</style>