<template>
  <div>
    <DetailModal v-if="modal" :id="randomPoster[Index].movie_id" :times="$route.params.times" @close="closeModal"/>
    <div class="rerecommend" @click="suffle"><i class="fa-solid fa-shuffle"></i></div>
    <section class="recommend-body">
          <div class="card-box">
            <div class="movie-card">
              <div class="movie-cardImg img1" @click="goToDetail(0)" @mousemove="cardOver1">
                <img :src="`https://www.themoviedb.org/t/p/original${randomPoster[0]?.poster_path}`">
              </div>
            </div>
      
            <div class="movie-card">
              <div class="movie-cardImg img2" @click="goToDetail(1)" @mousemove="cardOver2">
                <img :src="`https://www.themoviedb.org/t/p/original${randomPoster[1]?.poster_path}`">
              </div>
            </div>
      
            <div class="movie-card">
              <div class="movie-cardImg img3" @click="goToDetail(2)" @mousemove="cardOver3">
                <img :src="`https://www.themoviedb.org/t/p/original${randomPoster[2]?.poster_path}`">
              </div>
            </div>
          </div>
          
          <div class="card-box">
            <div class="movie-card">
              <div class="movie-cardImg img4" @click="goToDetail(3)" @mousemove="cardOver4">
                <img :src="`https://www.themoviedb.org/t/p/original${randomPoster[3]?.poster_path}`">
              </div>
            </div>
      
            <div class="movie-card">
              <div class="movie-cardImg img5" @click="goToDetail(4)" @mousemove="cardOver5">
                <img :src="`https://www.themoviedb.org/t/p/original${randomPoster[4]?.poster_path}`">
              </div>
            </div>
      
            <div class="movie-card">
              <div class="movie-cardImg img6" @click="goToDetail(5)" @mousemove="cardOver6">
                <img :src="`https://www.themoviedb.org/t/p/original${randomPoster[5]?.poster_path}`">
              </div>
            </div>
          </div>
    
    </section>
  </div>
</template>


<script>
import DetailModal from '@/components/DetailModal'
import _ from 'lodash'

export default {
  name: 'RecommendView',
  components: {
    DetailModal,
  },
  computed: {
    randomPoster() {
      const movies = this.$store.getters.randomPoster
      const times = this.$route.params.times
      const idx = this.$store.state.timesTable[times]
      return _.sampleSize(movies[idx], 6)
    },
    modal() {
      const bodyTag = document.querySelector('body')
      const modal = this.$store.state.modal
      if (modal === true) {
        bodyTag.style.overflow = 'hidden'
      } else {
        bodyTag.style.overflow = ''
      }
      return this.$store.state.modal
    }
  },
  data() {
    return {
      // modal: false,
      Index: null
    }
  },
  methods: {
    goToDetail(movieIndex) {
      this.Index = movieIndex
      // this.$router.push({ name: 'detail', params: { id: this.randomPoster[movieIndex].movie_id, times: this.$route.params.times } })
      // this.modal = true
      this.$store.commit('MODAL', true)

    },
    openModal() {
      // this.modal = true
      this.$store.commit('MODAL', true)
    },
    closeModal() {
      // this.modal = false
      this.$store.commit('MODAL', false)
      // this.$store.state.modal = false
    },
    cardOver1(event) {
      const docStyle = document.documentElement.style;
      docStyle.setProperty('--mouse-x1', event.clientX);
      docStyle.setProperty('--mouse-y1', event.clientY);
    },
    cardOver2(event) {
      const docStyle = document.documentElement.style;
      docStyle.setProperty('--mouse-x2', event.clientX);
      docStyle.setProperty('--mouse-y2', event.clientY);
    },
    cardOver3(event) {
      const docStyle = document.documentElement.style;
      docStyle.setProperty('--mouse-x3', event.clientX);
      docStyle.setProperty('--mouse-y3', event.clientY);
    },
    cardOver4(event) {
      const docStyle = document.documentElement.style;
      docStyle.setProperty('--mouse-x4', event.clientX);
      docStyle.setProperty('--mouse-y4', event.clientY);
    },
    cardOver5(event) {
      const docStyle = document.documentElement.style;
      docStyle.setProperty('--mouse-x5', event.clientX);
      docStyle.setProperty('--mouse-y5', event.clientY);
    },
    cardOver6(event) {
      const docStyle = document.documentElement.style;
      docStyle.setProperty('--mouse-x6', event.clientX);
      docStyle.setProperty('--mouse-y6', event.clientY);
    },
    suffle() {
      history.go(0)
    }
  },
  // created() {
  //   const bodyTag = document.querySelector('body')
  //   bodyTag.style.backgroundColor = '#eae9e4'
  // }
}
</script>

<style>

body {
  background-color: #eae9e4 !important;
}

.recommend-body {
  padding: 3vh 3vw;
  position: fixed;
  top: 0px;
  left: 0px;
  right: 0px;
  bottom: 0px;
  height: 94vh;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  z-index: 5;
  /* width: 100%; */
}

/* .recommend-box {
  display: flex;
  justify-content: center;
  align-items: center;
} */

.card-box {
  display: flex;
  position: relative;
  top: 0px;
  left: 0px;
  height: 40vh;
  justify-content: space-evenly;
}

.recommend-movies {
  display: flex;
  flex-direction: column;
}

/* 
31 0 0
0 0 0
-32 0 0

22
*/

.recommend-body > div:nth-child(1) > div:nth-child(1) {
  transform: translate3d(38vw, 22vh, 0px) rotate(-3.72973deg);
  animation: card-center1 2s forwards;
}

@keyframes card-center1 {
  0%{

  }
  100%{
    transform: translate3d(7vw, -1.0084vh, 0px) rotate(-3.72973deg);
  }
}

.recommend-body > div:nth-child(1) > div:nth-child(2) {
  transform: translate3d(7vw, 22vh, 0px) rotate(2.96006deg);
  animation: card-center2 2s 0.5s forwards;
}



@keyframes card-center2 {
  0%{

  }
  100%{
    
  transform: translate3d(7vw, -4vh, 0px) rotate(2.96006deg);
  }
}

.recommend-body > div:nth-child(1) > div:nth-child(3) {
  transform: translate3d(-25vw, 22vh, 0px) rotate(-3.36979deg);
  animation: card-center3 2s 1s forwards;
}

@keyframes card-center3 {
  0%{

  }
  100%{
    
  transform: translate3d(7vw, -2vh, 0px) rotate(-3.36979deg);
  }
}

.recommend-body > div:nth-child(2) > div:nth-child(1) {
  transform: translate3d(38vw, -22vh, 0px) rotate(3.72973deg);
  animation: card-center4 2s 1.5s forwards;
}

@keyframes card-center4 {
  0%{

  }
  100%{
    
  transform: translate3d(7vw, -1vh, 0px) rotate(3.72973deg);
  }
}

.recommend-body > div:nth-child(2) > div:nth-child(2) {
  transform: translate3d(7vw, -22vh, 0px) rotate(-4.83002deg);
  animation: card-center5 2s 2s forwards;
}

@keyframes card-center5 {
  0%{

  }
  100%{
    
  transform: translate3d(7vw, 0vh, 0px) rotate(-4.83002deg);
  }
}

.recommend-body > div:nth-child(2) > div:nth-child(3) {
  transform: translate3d(-25vw, -22vh, 0px) rotate(2.59983deg);
  animation: card-center6 2s 2.5s forwards;
}

@keyframes card-center6 {
  0%{

  }
  100%{
    
    transform: translate3d(7vw, -3vh, 0px) rotate(2.59983deg);
  }
}

img {
  height: 100%;
  width: 100%;
}

.img1:hover {
  transform:
  translateX(calc(var(--mouse-x1) * 0.1px))
  translateY(calc(var(--mouse-y1) * 0.1px));
}

.img2:hover {
  transform:
  translateX(calc(var(--mouse-x2) * 0.05px))
  translateY(calc(var(--mouse-y2) * 0.05px));
}

/* .movie-cardImg:nth-child(2):hover {
  transform:
  translateX(calc(var(--mouse-x2) * 0.2px))
  translateY(calc(var(--mouse-y2) * 0.2px));
} */

.img3:hover {
  transform:
  translateX(calc(var(--mouse-x3) * 0.02px))
  translateY(calc(var(--mouse-y3) * 0.02px));
}

.img4:hover {
  transform:
  translateX(calc(var(--mouse-x4) * 0.1px))
  translateY(calc(var(--mouse-y4) * 0.07px));
}

.img5:hover {
  transform:
  translateX(calc(var(--mouse-x5) * 0.05px))
  translateY(calc(var(--mouse-y5) * 0.05px));
}

.img6:hover {
  transform:
  translateX(calc(var(--mouse-x6) * 0.03px))
  translateY(calc(var(--mouse-y6) * 0.03px));
}

.movie-cardImg:hover img {
  filter: grayscale(0) brightness(1);

}

.movie-cardImg:hover {
  animation: card 2s forwards;
}

@keyframes card {
  0%{

  }
  100%{
    transform: ranslate3d(2.1978px, -48.4001px, 0px) rotate(2.59983deg);
  }
}





.movie-card{
  /* display: flex; */
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 33%;
  border-radius: 1rem;
  overflow: hidden;
  overflow-x: hidden;
  overflow-y: hidden;
  position: relative;
  top: 0px;
  left: 0px;
  animation: card-center 3s forwards;
}



.movie-card:before {
    content: "";
    position: absolute;
    top: 35%;
    right: -25%;
    border-radius: 1rem;
    /* background-color: red; */
    /* background-color: #525252; */
    opacity: .3;
    filter: blur(28px);
    width: 50%;
    height: 50%;
    z-index: -1;
}

.movie-cardImg {
  display: flex;
  justify-content: center;
  align-items: center;  
  height: 21rem;
  width: 14rem;
  border-radius: 1rem;
  overflow: hidden;
  overflow-x: hidden;
  overflow-y: hidden;
  position: relative;
}

.movie-cardImg img {
  display: block;
  filter: grayscale(1) brightness(0.7);
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  transition: filter 1s cubic-bezier(0.215, 0.61, 0.355, 1);
}

.movie-cardImg:after {
    transition: opacity .5s cubic-bezier(0.215, 0.61, 0.355, 1);
    opacity: 0;
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(0deg, rgba(0, 0, 0, 0.8) 0%, rgba(0, 0, 0, 0) 100%);
}

.rerecommend {
  background-color: #e9e9e97a;
  color: #1f1f1f;
  width: 8vh;
  height: 8vh;
  font-size: 4rem;
  text-align: center;
  position: absolute;
  top: 42vh;
  left: 47vw;
  border-radius: 10px;
  cursor: pointer;
  z-index: 6;
  animation: suffle 6s forwards;
}

@keyframes suffle {
  0%{
    opacity: 0;
  }
  80%{
    opacity: 0;
  }
  100%{
    opacity: 1;
  }
}
</style>