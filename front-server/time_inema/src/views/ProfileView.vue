<template>
  <section class="profile-body">
    <div class="profile">
      <h1>Profile</h1>
      <div class="profile-back">
        
      </div>
      <div class="profile-user">
        <img :src="user.img">
        <h2>{{ user.name }}</h2>
      </div>
      <div class="profile-like">
        <h2>좋아요한 영화</h2>
        <p>좋아요한 영화가 없어요...</p>
      </div>
      <div class="profile-review">
        <h2>내가 남긴 리뷰</h2>
        <p v-if="reviews.length === 0">아직 리뷰가 없어요...</p>
        <ReviewItem 
          v-for="review in reviews"
          :key="review.id"
          :review="review"
        />
      </div>

    </div>
  </section>
</template>

<script>
import ReviewItem from '@/components/ReviewItem'

export default {
  name: 'ProfileView',
  components: {
    ReviewItem,
  },
  computed: {
    user() {
      return {
        id: 1,
        name: '김싸피',
        img: 'https://www.freeiconspng.com/thumbs/profile-icon-png/profile-icon-9.png'
      }
    },
    reviews() {
      const reviews = this.$store.state.reviews
      console.log(reviews.filter(review => review.userId === this.user.id))
      return reviews.filter(review => review.userId === this.user.id)
    }
  }

}
</script>

<style scoped>
body {
  background-color: #1c1c1c;
}

.profile {
  display: flex;
  /* justify-content: center; */
  margin-top: 0px;
  flex-direction: column;
  position: fixed;
  /* top: 3vh;
  left: 10vw;
  right: 10vw;
  bottom: 0vh; */
  top: 10vh;
  left: 20vw;
  right: 20vw;
  bottom: 10vh;
  overflow: scroll;
  border-radius: 10px;
  background-color: #eae9e4;
}

.profile > h1 {
  font-size: 50px;
  font-weight: 600;
}
/* .profile-back {
  background-color: rebeccapurple;
  height: 30vh;
  width: 100%;
} */

.profile-user {
  display: flex;
  margin-left: 10vw;

}

.profile-user > h2 {
  text-align: start;
  margin-left: 20px;
}

.profile-user > img {
  height: 80px;
  width: 80px;
  background-color: rgb(252, 245, 235);
  border-radius: 100px;
}

.profile-like {
  display: flex;
  flex-direction: column;
  margin-left: 10vw;
  align-items: start;
}

.profile-review {
  display: flex;
  flex-direction: column;
  margin-left: 10vw;
  align-items: start;

}

</style>