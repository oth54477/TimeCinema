<template>
  <section class="review-item-body">
    <div class="review-item">
      <div>
        <img :src="`http://192.168.212.86:8000${review.user?.profile_image}`">
      </div>
      <div>
        <div>
          <h3>{{ review.user?.username }}</h3>
          <div>
            <div v-for="index in this.review.star_point" :key="index" class="fa fa-solid fa-star" style="color:yellow; font-size: 1.1rem;"></div>
          </div>
        </div>
        <p>{{ this.review.comment_content }}</p>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'ProfileReview',
  props: {
    review: Object,
  },
  computed: {
    // user() {
    //   const userId = this.review.user
    //   const test = this.$store.dispatch('getUserProfile', userId)
    //   console.log('유저아이디',userId)
    //   console.log('엑시오스',test)
    //   return this.$store.state.userInfo.find(user => user.id === this.review.userId)
    // }
  },
  // methods
}
</script>

<style>
.review-item-body {
  display: flex;
  align-items: center;
}


.review-item {
  display: flex;
  align-items: center;
  margin-bottom: 30px;
}

.review-item > div:nth-child(1) {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.review-item > div:nth-child(1) > img {
  height: 80px;
  width: 80px;
  background-color: rgb(252, 245, 235);
  border-radius: 10px;
}

.review-item > div:nth-child(2) {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
  margin-left: 20px;
}

.review-item > div:nth-child(2) > p {
  margin: 0px;
}

.review-item > div:nth-child(2) > div {
  display: flex;
  align-items: center;

}

.review-item > div:nth-child(2) > div > div {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-left: 20px;
}

#app > section > div > div.profile-review > section > div > div > img {
 border-radius: 100px;
 width: 50px;
 height: 50px;
}

#app > section > div > div.profile-review > section > div > div {
  font-size: 0.8rem;
}
</style>