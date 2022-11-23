<template>
  <div>
    <DetailModal v-if="modal" :id="randomPoster[Index].movie_id" :times="$route.params.times" @close="closeModal"/>
    <section class="recommend-body">
      <div class="recommend-box">
        <div class="recommend-movies">
    
          <div class="movie-card" @click="goToDetail(0)">
            <div class="movie-cardImg">
              <img :src="`https://www.themoviedb.org/t/p/original${randomPoster[0]?.poster_path}`">
            </div>
          </div>
    
          <div class="movie-card" @click="goToDetail(1)">
            <div class="movie-cardImg">
              <img :src="`https://www.themoviedb.org/t/p/original${randomPoster[1]?.poster_path}`">
            </div>
          </div>
    
          <div class="movie-card" @click="goToDetail(2)">
            <div class="movie-cardImg">
              <img :src="`https://www.themoviedb.org/t/p/original${randomPoster[2]?.poster_path}`">
            </div>
          </div>
    
          <div class="movie-card" @click="goToDetail(3)">
            <div class="movie-cardImg">
              <img :src="`https://www.themoviedb.org/t/p/original${randomPoster[3]?.poster_path}`">
            </div>
          </div>
    
          <div class="movie-card" @click="goToDetail(4)">
            <div class="movie-cardImg">
              <img :src="`https://www.themoviedb.org/t/p/original${randomPoster[4]?.poster_path}`">
            </div>
          </div>
    
          <div class="movie-card" @click="goToDetail(5)">
            <div class="movie-cardImg">
              <img :src="`https://www.themoviedb.org/t/p/original${randomPoster[5]?.poster_path}`">
            </div>
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
  name: 'RecommendView3',
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
  padding: 3vh 10vw;
  position: fixed;
  top: 0px;
  left: 0px;
  right: 0px;
  bottom: 0px;
  height: 100%;
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

.recommend-movies {
  display: grid;
  grid-template-rows: 5fr 1fr 5fr;
  grid-template-columns: 10fr 1fr 10fr 1fr 10fr;
  /* height: 70vh; */
  /* grid-template-areas: "card1 . card2 . card3"
  "none none none none none"
  "card4 . card5 . card6"; */
}


.recommend-body div:nth-child(1) {
  /* grid-area: card1; */
  grid-column-start: 1;
  grid-column-end: 2;
  grid-row-start: 1;
  grid-row-end: 2;
  /* transform: translate3d(-1.8911px, -29.0084px, 0px) rotate(-3.72973deg); */
}

.recommend-body div:nth-child(2) {
  /* grid-area: card2; */
  grid-column-start: 3;
  grid-column-end: 4;
  grid-row-start: 1;
  grid-row-end: 2;
  transform: translate3d(2.5019px, -28.3854px, 0px) rotate(2.96006deg);
}

.recommend-body div:nth-child(3) {
  /* grid-area: card3; */
  grid-column-start: 5;
  grid-column-end: 6;
  grid-row-start: 1;
  grid-row-end: 2;
  transform: translate3d(-2.2785px, -38.693px, 0px) rotate(-3.36979deg);
}

.recommend-body div:nth-child(4) {
  /* grid-area: card4; */
  grid-column-start: 1;
  grid-column-end: 2;
  grid-row-start: 3;
  grid-row-end: 4;
  transform: translate3d(1.576px, 24.1737px, 0px) rotate(3.72973deg);
}

.recommend-body div:nth-child(5) {
  /* grid-area: card5; */
  grid-column-start: 3;
  grid-column-end: 4;
  grid-row-start: 3;
  grid-row-end: 4;
  /* transform: translate3d(3.6715px, 43.4502px, 0px) rotate(-4.83002deg); */
  transform: translate3d(3.6715px, 0px, 0px) rotate(-4.83002deg);
}

.recommend-body div:nth-child(6) {
  /* grid-area: card6; */
  grid-column-start: 5;
  grid-column-end: 6;
  grid-row-start: 3;
  grid-row-end: 4;
  transform: translate3d(2.1978px, -48.4001px, 0px) rotate(2.59983deg);
}

img {
  height: 100%;
  width: 100%;
}

.movie-card:hover img {
  filter: grayscale(0) brightness(1);

}

.movie-card:hover {
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
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
  border-radius: 1rem;
  overflow: hidden;
  overflow-x: hidden;
  overflow-y: hidden;
  position: relative;
  
  

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
  height: 25rem;
  width: 17rem;
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
</style>