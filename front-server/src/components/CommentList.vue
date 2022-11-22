<template>
  <div>
    <br><br>
    <br><br>
    <div class="container">
    <CommentListItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
    />
    
    </div>
    </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem'
export default {
  name: 'CommentList',
  components:{
    CommentListItem,
  },
  props:{
    comments: Array,
  },
}
</script>

<style scoped>
.container {
  overflow: auto;
  float: left;
  margin-top: -35px;
  border-radius: 20px;
  width: 1175px;
  height: 120px;
}

.container::-webkit-scrollbar {
    width: 10px;
  }

.container::-webkit-scrollbar-thumb {
    background-color: red;
    border-radius: 10px;
    
  }


.container::-webkit-scrollbar-track {
    background-color: lightgrey;
    border-radius: 10px;
    box-shadow: inset 0px 0px 5px grey;
  }
</style>