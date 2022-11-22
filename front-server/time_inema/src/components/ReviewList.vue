<template>
  <section class="review-list-body">
    <ReviewItem 
      v-for="review in reviews"
      :key="review.id"
      :review="review"
    />
  </section>
</template>

<script>
import ReviewItem from '@/components/ReviewItem'

export default {
  name: 'ReviewList',
  components: {
    ReviewItem,
  },
  props: {
    reviews: Array,
  },
  computed: {

  }
}
</script>

<style>

</style>