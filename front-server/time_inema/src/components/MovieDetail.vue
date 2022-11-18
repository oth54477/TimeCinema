<template>
  <section class="detail-body">
    <h1>Detail</h1>
    <div class="movie-detail">
      <div class="poster-img">
        <img :src="`https://www.themoviedb.org/t/p/original${movie.poster_path}`">
      </div>
      <div class="movie-info">
        <div>
          <h2>제목: {{ movie.title }}</h2>
          <h2>줄거리: {{ movie.overview }}</h2>
          <h2>장르: {{ movie.genre_ids.map(genre => genre.name) }}</h2>
        </div>
        <div>
          <input type="text">
        </div>
      </div>
    </div>
    
  </section>
</template>

<script>
export default {
  name: 'MovieDetail',
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
    movie() {
      const payload = {
        id: this.id,
        times: this.times
      }
      const movie =  this.$store.getters.movieDetail(payload)
      console.log('영화 디테일', movie)
      return movie
    },
  },
  data() {
    return {
    }
  },
  methods: {

  },
}
</script>

<style>
.detail-body {
  padding: 5vh 5vw;
  color: antiquewhite;
  position: relative;
}

.movie-detail {
  display: flex;
  margin-top: 5vh;
}

.poster-img {
  flex-basis:25%;
  flex-shrink: 0;
  margin: 3vh 3vw;
  display: flex;
  justify-content: center;
  align-items: center;
}

.movie-info {
  flex-grow: 1;
  margin: 3vh 3vw;
  display: flex;
  flex-direction: column;
  align-items: start;
}



.poster-img img {
  /* height: 20rem; */
  /* width: 15rem; */
  /* height: 100%; */
  width: 100%;

}
</style>