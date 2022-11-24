<template>
  <section class="profile-body">
    <div class="profile">
      <h1>Profile</h1>
      <div class="profile-back">
        
      </div>
      <div class="profile-user">
        <img :src="`http://192.168.212.86:8000${user.profile_image}`">
        <!-- <img :src="`${process.env.VUE_APP_DJANGO_API_URL}${user.profile_image}`"> -->
        <h2>{{ user.username }}</h2>
      </div>
      <div class="profile-like">
        <h2>좋아요한 영화</h2>
        <p v-if="reviews?.length === 0">좋아요한 영화가 없어요...</p>
        <div class="like-box">
          <ProfileLike 
            v-for="like in likes"
            :key="like.id"
            :like="like"
          />
        </div>
      </div>
      <div class="profile-review">
        <h2>내가 남긴 리뷰</h2>
        
        <ProfileReview 
          v-for="review in reviews"
          :key="review.id"
          :review="review"
        />
      </div>

    </div>
  </section>
</template>

<script>
import ProfileReview from '@/components/ProfileReview'
import ProfileLike from '@/components/ProfileLike'
import axios from 'axios'
import SERVER from '@/api/drf.js'

const DJANGO_API_URL = SERVER.URL

export default {
  name: 'ProfileView',
  components: {
    ProfileReview,
    ProfileLike,
  },
  computed: {
    // user() {
    //   return 1
    // },
    // reviews() {
    //   const reviews = this.$store.state.reviews
    //   console.log(reviews.filter(review => review.userId === this.user.id))
    //   return reviews.filter(review => review.userId === this.user.id)
    // },
    token() {
      return this.$store.state.token
    },
    userList() {
      return this.$store.state.userList
    }
  },
  data() {
    return {
      id: null,
      user: null,
      reviews: null,
      likes: null,
    }
  },
  methods: {
    findUserInfo() {
      const user = this.userList.find(user => user.id === this.id)
      console.log('현재 유저', user)
      this.user = user
    },
  },
  created() {
    // const DJANGO_API_URL = "http://192.168.212.86:8000"
    axios({
      method: 'get',
      url: `${DJANGO_API_URL}/accounts/user/`,
      headers: {
        Authorization: `Token ${this.token}` 
      }
    })
      .then((res) => {
        this.id = res.data.pk
        this.findUserInfo()
        axios({
          method: 'get',
          url: `${DJANGO_API_URL}/movies/comment/${this.user.id}`,
        })
          .then((res) => {
            console.log('리뷰',res)
            this.reviews = res.data
          })
          .catch((error) => {
            console.log(error)
          })
        axios({
          method: 'get',
          url: `${DJANGO_API_URL}/movies/like/${this.user.id}`,
        })
          .then((res) => {
            console.log('좋아요',res)
            this.likes = res.data
          })
          .catch((error) => {
            console.log(error)
          })
      })

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




.profile > h1 {
  text-align: center;
}

.profile-like {
  text-align: center;
}
.like-box {
  display: flex;
  align-content: center;
  justify-content: center;
  flex-wrap: wrap;
  width: 45vw;
}
</style>