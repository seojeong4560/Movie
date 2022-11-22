<template>
  <div id="cmitem" >
    <p id="cmfont1">{{ comment.username}}</p>
    <p id="cmfont11">님</p>
    <p id="cmfont2">{{ comment.content }}</p>
    <!-- <p id="cmfont3">수정</p> -->
    <br><br><br><br>
    <p id="cmfont3">{{ comment.created_at }}</p>
    <button @click="deleteComment" id="cmbtn" class="btn btn-light"><p id="delword">삭제</p></button>
    <br><hr>
    <br>
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

<style scoped>
/* #cmitem{
  background-color: rgba(117, 115, 115, 0.5);
  float: left;
  margin-top: -55px;
  border-radius: 20px;
  width: 775px;
  height: 120px;
} */

#cmfont1{
  color: red;
  -webkit-text-stroke: 0.5px black;
  font-weight: bold;
  float: left;
  margin-top: 20px;
  /* margin-left: 10px; */
  font-size: 30px;
}

#cmfont11{
  color: white;
  float: left;
  margin-top: 35px;
  /* margin-left: 10px; */
  font-size: 18px;
  font-weight: bold;
}

#cmfont2{
  color: white;
  float: left;
  margin-top: 30px;
  margin-left: 40px;
  font-size: 25px;
}

#cmfont3{
  color: white;
  float: left;
  /* margin-left: 10px; */
  font-size: 15px;
  /* margin-top: 100px; */
  /* float: bottom; */
  
}

#cmbtn{
  /* margin-top: 35px; */
  margin-left: 10px;
  float: left;
  width: 50px;
  height: 25px;
  
}

#delword{
  float: left;
  font-size: 10px
}





</style>