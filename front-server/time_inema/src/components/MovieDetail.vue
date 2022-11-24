<template>
  <section class="detail-body">
    <div class="movie-detail">
      <div class="poster-img">
        <!-- <div class="video-box" data-vbg-autoplay="true" :data-vbg="`https://www.youtube.com/embed/${ this.trailers[0].url }?autoplay=1&mute=1`"></div> -->
        <!-- <img :src="`https://www.themoviedb.org/t/p/original${movie.poster_path}`"> -->
        <iframe class="video" frame  :src="`https://www.youtube.com/embed/${ this.trailers[0]?.url }?autoplay=1&mute=1&loop=1&controls=0&vq=hd1080&rel=0`" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture;" allowfullscreen></iframe>
        <!-- <div data-vbg="https://www.youtube.com/watch?v=eEpEeyqGlxA"></div> -->

      </div>
      <div class="article">
        <div class="movie">
          <div>
            <img :src="`https://www.themoviedb.org/t/p/original${movie.poster_path}`">
            <div>
              <div class="movie-title">
                <h1 class="title">{{ movie.title }}</h1>

              </div>
              <div class="user-movie">
                <div class="movie-stars">
                  <div 
                    v-for="index in 5"
                    :key="index"
                    @mouseover="starOver(index)"
                    @mouseleave="starLeave"
                    @click="starClick(index)"
                  >
                    <div v-if="index < score+1"><div class="fa fa-solid fa-star" style="color:yellow;"></div></div>
                    <div v-if="index >= score+1"><div class="fa fa-solid fa-star"></div></div>
                  </div>
                </div>

                <div 
                  class="like-movie"
                  @click="heartClick"
                >
                  <div
                    @click="like"
                    @mouseover="heartOver"
                    @mouseleave="heartLeave"
                    v-if="!isheartClicked"
                    :class="{ movieHeart: isheart, movieHeartNone: !isheart }"
                  >
                    <!-- <div v-if="isheart"  class="fa fa-solid fa-heart heart-div"></div> -->
                    <div  class="fa fa-regular fa-heart heart-div"></div>
                    <p class="geart-p">좋아하는 항목에 추가</p>
                  </div>
                  <div
                  @click="like"
                  class="movieHeart" 
                  v-if="isheartClicked" 
                  >
                    <div class="fa fa-solid fa-heart heart-div"></div>
                    <p class="geart-p">좋아하는 항목에 추가됨</p>
                  </div>
                  
                </div>






                
              </div>
            </div>
          </div>
          <div class="movie-info">
            <div class="main-detail">
              <p class="content">{{ movie.overview }}</p>
              <div class="crew">
                <CrewList 
                  :casts="casts"
                />
              </div>
            </div>
            <div class="movie-infos">
              <div class="subContent">
                <p>{{ movie.release_date.split('-')[0] }}</p>
                <p class="genre"><span v-for="(a, index) in movie.genre_ids.map(genre => genre.name)" :key="index">{{ a }} </span></p>
                <hr>
              </div>
              <div class="people">
                <p>같이볼 사람 {{ movie.watch_users.length }}명</p>
                <div class="fa fa-solid fa-user-plus watch-class" @click="watchClick" :class="{ 'watch-user-color': isWatch }"></div>
              </div>
              <div class="watch-users">
                <WatchUserList :watchUsers="movie.watch_users"/>
              </div>
            </div>
          </div>
        </div>
        <div class="review">
          <!-- <input type="text"> -->
          <div>
            <h1>사용자 리뷰</h1>
            <p style="margin-left:10px; margin-top: 25px;">{{ reviews.length }}개</p>
            
            <!-- <button class="btn-review" @click="clickReview">리뷰 쓰기</button>  -->
            <div class="fa fa-solid fa-pen-to-square" @click="clickReview"></div>
          </div>
          <div class="review-input" v-if="this.isclickedReview">
            <div class="stars">
              <div 
              v-for="index in 5"
              :key="index"
              @mouseover="starOver(index)"
              @mouseleave="starLeave"
              @click="starClick(index)"
              >
              <div v-if="index < score+1"><div class="fa fa-solid fa-star" style="color:#ffeb00;"></div></div>
              <div v-if="index >= score+1"><div class="fa fa-solid fa-star"></div></div>
            </div>
          </div>
          <div>
            <textarea name="" id="" cols="100%" rows="10" v-model="content"></textarea>
          </div>
          <div class="upload" @click="createReview">
            <p>작성하기</p>
            <div class="fa fa-solid fa-upload"></div>
          </div>
        </div>
        <div v-if="reviews.length === 0" style="margin-bottom:30px;">
            <h1>첫 리뷰를 남겨주세요!</h1>
        </div>
          <ReviewList :reviews="reviews"/>  
          <div class="footer_space"></div>
        </div>
      </div>
    </div>
    
  </section>
</template>

<script>
import ReviewList from '@/components/ReviewList'
import CrewList from '@/components/CrewList'
import WatchUserList from '@/components/WatchUserList'

import axios from 'axios'
import SERVER from '@/api/drf.js'
// import VideoBackgrounds from 'https://unpkg.com/youtube-background@1.0.14/jquery.youtube-background.min.js'
// const DJANGO_API_URL = "http://127.0.0.1:8000"
// const DJANGO_API_URL = "http://192.168.212.86:8000"

const DJANGO_API_URL = SERVER.URL
const TMDB_API_KEY = process.env.VUE_APP_TMDB_API_KEY
const TMDB_API_URL = process.env.VUE_APP_TMDB_API_URL

export default {
  name: 'MovieDetail',
  components: {
    ReviewList,
    CrewList,
    WatchUserList,
  },
  props: {
    id: Number,
    times: String,
  },
  computed: {
    // id() {
    //   return this.$route.params.id
    // },
    // times() {
    //   return this.$route.params.times
    // },
    movies() {
      return this.$store.state.movies
    },
    // movie() {
    //   const payload = {
    //     id: this.id,
    //     times: this.times
    //   }
    //   const movie =  this.$store.getters.movieDetail(payload)
    //   console.log('영화 디테일', movie)
    //   return movie
    // },
    trailers() {
      const trailers = this.$store.state.trailers
      return trailers
    },
    reviews() {
      const reviews = this.dataReviews
      console.log('리뷰 불러옴', reviews)
      return reviews
      // return reviews.filter(review => review.id === this.id)
    },
    user() {
      return this.$store.state.user
    }
  },
  data() {
    return {
      movie: null,
      dataReviews: null,
      score: 0,
      isheart: false,
      isheartClicked: false,
      isStarClicked: false,
      isclickedReview: false,
      content: null,
      casts: null,
      isWatch: false,
      watchUser: {
        color: '#288ce1'
      },
    }
  },
  methods: {
    starClick(index) {
      if (this.score === index) {
        this.isStarClicked = !this.isStarClicked
      } else {
        this.score = index
      }
    },
    starOver(index) {
      if (!this.isStarClicked) {
        this.score = index;
      }
    },
    starLeave() {
      if (!this.isStarClicked) {
        this.score = 0
      }
    },
    heartClick() {
      this.isheartClicked = !this.isheartClicked
    },
    heartOver() {
      if (!this.isheartClicked) {
        this.isheart = true
      }
    },
    heartLeave() {
      if (!this.isheartClicked) {
        this.isheart = false
      }
    },
    clickReview() {
      console.log('리뷰리뷰', this.dataReviews)
      console.log('리뷰리뷰', this.user.id)
      if (this.dataReviews.find(review => review.user.id === this.user.id)) {
        window.alert('이미 리뷰를 작성했습니다!')
      } else {
        this.isclickedReview = !this.isclickedReview
      }
    },
    createReview() {
      // 리뷰 업로드
  
      const payload = {
        movieId: this.id, 
        score: this.score, 
        content: this.content,
      }
      axios({
        method: 'post',
        url: `${DJANGO_API_URL}/movies/${payload.movieId}/comment/create`,
        headers: {
          Authorization: `Token ${this.$store.state.token}` 
        },
        data: {
          movie: payload.movieId,
          star_point: payload.score, 
          comment_content: payload.content,
        }
      })
        .then((res) => {
          console.log(res)
          this.isclickedReview = false
          this.getReviews()

        })
      // this.$store.dispatch('createComment', )
    },
    getReviews() {
      axios({
        method: 'get',
        url: `${DJANGO_API_URL}/movies/${this.id}/comment`,
      })
        .then((res) => {
          console.log('리뷰 불러옴',res)
          this.dataReviews = res.data
          const userReview = res.data.find(review => review.user.id === this.user.id)
          if (userReview) {
            this.isStarClicked = true
            this.score = userReview.star_point
          }
        })
        .catch((error) => {
          console.log(error)
        })
    },
    like() {
      axios({
        method: 'post',
        url: `${DJANGO_API_URL}/movies/${this.id}/like`,
        headers: {
          Authorization: `Token ${this.$store.state.token}` 
        },
      })
        .then((res) => {
          console.log('like', res)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getDetail() {
      axios({
        method: 'get',
        url: `${DJANGO_API_URL}/movies/${this.id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}` 
        },
      })
        .then((res) => {
          console.log('영화 디테일', res)
          this.movie = res.data
          if (res.data.like_users.find(likeUser => likeUser.id === this.user.id)) {
            this.isheartClicked = true
          } else {
            this.isheartClicked = false
          }
          if (res.data.watch_users.find(user => user.id === this.user.id)) {
            this.isWatch = true
          } else {
            this.isWatch = false
          }

        })
        .catch((error) => {
          console.log(error)
        })
    },
    getCrews() {
      axios({
        method: 'get',
        url: `${TMDB_API_URL}/${this.id}/credits`,
        params: {
                api_key: TMDB_API_KEY,
                language: 'ko-KR',
                },    
      })
        .then((res) => {
          console.log('스탭', res.data)
          this.casts = res.data.cast
          // this.crew = res.data.crew
        })
    },
    watchClick() {
      this.isWatch = !this.isWatch
      console.log(this.isWatch)
      axios({
        method: 'post',
        url: `${DJANGO_API_URL}/movies/${this.id}/watch`,
        headers: {
          Authorization: `Token ${this.$store.state.token}` 
        },
      })
        .then((res) => {
          console.log(res)
          this.getDetail()
        })
        .catch((error) => {
          console.log('같이볼 유저', error)
        })
    }
  },
  created() {
    this.getDetail()
    this.$store.dispatch('getTrailer', {id: this.id})
    this.getReviews()
    this.getCrews()
    // const content = document.querySelector('.content')
    // const contentH = content.offsetHeight

    // const 

    // const docStyle = document.documentElement.style;
    //   docStyle.setProperty('--mouse-x1', event.clientX);
  },
  update() {
    this.getReviews()
  }
}
</script>

<style>
.detail-body {
  padding: 5vh 5vw;
  color: antiquewhite;
  position: relative;
  padding: 0px;
}

.movie-detail {
  display: flex;
  margin-top: 0px;
  flex-direction: column;
  position: fixed;
  top: 3vh;
  left: 10vw;
  right: 10vw;
  bottom: 0vh;
  overflow: scroll;
  /* border-radius: 10px; */
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  background-color: #201f1f;
}

.poster-img {
    flex-basis: 25%;
    flex-shrink: 0;
    /* margin: 3vh 3vw; */
    margin: 0px;
    display: flex;
    justify-content: center;
    height: 40vh;
    flex-basis: 40vh;
    /* background-color: black; */
    align-items: center;
    /* background-color: balck; */
    /* background: linear-gradient(180deg, transparent, #201f1f); */
}

.movie {
    /* flex-grow: 1; */
    /* margin: 3vh 3vw; */
    display: flex;
    flex-direction: column;
    /* justify-content: start; */
    /* align-items: start; */
    /* position: absolute; */
    /* top: 40vh; */
    /* left: 0vw; */
    height: 100%;
    width: 90%;
    margin: 0px;
    text-align: start;
    /* padding: 50px; */
    /* background-color: #201f1f; */
    z-index: -1;
    /* background-color: #201f1f; */
    /* padding-top: 25vh; */
    color: white;
    padding: 0vh 2.5vw;
}



.poster-img img {
    /* height: 20rem; */
    /* width: 15rem; */
    height: 100%;
    object-fit: cover;
    object-position: top;
    /* width: 100%; */
    position: absolute;
    top: 0px;
    left: 0px;
    z-index: -1;
    border-radius: 5px;
}


.poster-img iframe {
    /* height: 20rem; */
    /* width: 15rem; */
    height: 100%;
    object-fit: cover;
    object-position: top;
    /* width: 100%; */
    position: absolute;
    top: 0px;
    /* top: -204px; */
    top: -10vh;
    /* top: 56.25%; */
    left: 0px;
    z-index: -1;
    border-radius: 5px;

    width: 100%;
    /* height: 1080px; */
    offset: 200;
    

}

.article {
  flex-grow: 1;
  margin: 3vh 3vw;
  display: flex;
  flex-direction: column;
  justify-content: start;
  /* align-items: start; */
  /* position: absolute; */
  top: 40vh;
  left: 0vw;
  height: 100%;
  width: 100%;
  margin: 0px;
  text-align: start;
  /* padding: 50px; */
  /* background-color: #201f1f; */
  z-index: -1;
  /* background-color: #201f1f; */
  /* padding-top: 25vh; */
  background: linear-gradient(0deg, #201f1f 80%, #201f1f00);
  color: white;
  padding: 0vh 2.5vw;
}

.movie > div > div > .title {
  font-size: 3rem;
}

.movie > div:nth-child(1) > div {
  margin-left: 30px;
  flex-basis: 100%;
}

.movie-info {
  display: flex;
  flex-direction: row;
  font-size: 20px;
  margin: 20px 10px 20px 10px;
}

.movie-info > div:nth-child(1) {
  flex-basis: 70%;
  line-height: 35px;

}


.movie-info > div:nth-child(2) {
  flex-basis: 30%;
  margin-left: 10px;
}

.review { 
  display: flex;
  /* position: absolute; */
  /* top: 0px; */
}

.user-movie {
  flex-basis: 40%;
  display: flex;
  align-items: center;
  /* margin-bottom: 55px; */
  justify-content: flex-start;
}

.movieHeart {
  height: 4vh;
  width: 15vw;
  border: solid 2.5px #454444;
  background-color: #454444;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.movieHeartNone {
  height: 4vh;
  width: 15vw;
  border: solid 2.5px #454444;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.heart-div {
  margin-right: 10px;
}

.heart-p {
  margin-left: 10px;
}
/* .movie-heart {
  margin-right: 10vw;
  display: flex;
  align-items: center;
  flex-wrap: nowrap;
} */

.movie > div:nth-child(1) {
  margin-bottom:1vh;
  display: flex;
  /* justify-content: space-between; */
  justify-content: flex-start;
  align-items: flex-end;
}

.movie-stars {
  display: flex;
}

.fa-star {
  /* color: yellow; */
  font-size: 40px;
}

.fa-heart {
  color: red;
  font-size: 1.8rem;

}

.movie > div > img {
  width: 10vw;
  border-radius: 5px;
  border: solid 4px rgb(164, 161, 161);
}

.review > div:nth-child(1) {
  display: flex;
  justify-content: start;
  align-items: center;
  vertical-align: baseline;
}

.review {
  display: flex;
  flex-direction: column;
  width: 90%;
  padding: 0vh 2.5vw;
}

.btn-review {
  height: 2rem;
} 

.fa-pen-to-square {
  color: white;
  font-size: 25px;
  margin-left: 20px;
  cursor: pointer;
}

.review-input {
  display: flex;
  margin: 10px 0px 30px 0px;
  flex-direction: column;
}

.stars > div > div > .fa-star {
  font-size: 2rem;
}

.stars {
  display: flex;
  margin-bottom: 2rem;
}

.upload {
  display: flex;
  justify-content: end;
  cursor: pointer;
}

.upload > .fa-upload {
  font-size: 2rem;
}

.upload > p {
  font-size: 1.5rem;
  margin: 8px 10px 0px 0px;
}

textarea {
  width: 100%;
  margin-bottom: 20px;
  font-size: 20px;
}

.movie-title {
  display: flex;
  align-items: center;
}

.movie-title > h1 {
  font-size: 50px;
}

/* .movie-title  > div {
  margin-left: 20px;
} */

.like-movie {
  margin-left: 2.5vw;
  margin-top: 1vh;
}

/* .movie-info > div > p {
  text-overflow: ellipsis;
  height: 25vh;
  width: 45vw;
  overflow: hidden;
  white-space: nowrap;
} */

.movie-infos {
  font-size: 20px;
  margin-top: 3vh;
  border: solid 1px #ffffff75;
  padding: 0px 10px;
  border-radius: 10px;
}

.subContent> hr {
  height: 0vh;
  width: 20.9vw;
  background-color: #ffffff36;
  border: solid 0.1px #ffffff75;
  margin: 3vh 0vw;
}

.subContent > p:nth-child(1) {
  font-size: 30px;
  margin-bottom: 0;
  margin-top: 0px;
}

.watch-users {
  padding: 20px;
  border: solid 2.5px #454444;
  border-radius: 10px;
  height: 39vh;
}

.crew {
  margin-top: 5vh;
}

.watch-class {
  margin: 0px 10px;
  font-size: 25px;

}

.watch-class:hover {
  animation: human 1s forwards;
}

@keyframes human {
  0% {

  }
  100% {
    color: #288ce1;
  }
}

.people {
  display: flex;
  align-items: center;
  
}

.watch-user-color {
  color: #288ce1;
}

.footer_space {
  height: 10vh;
}

</style>