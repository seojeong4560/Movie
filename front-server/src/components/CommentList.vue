<template>
  <div>
    <h4>List</h4>
    <CommentListItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
    />
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

<style>

</style>