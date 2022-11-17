<template>
  <div>
    <section class="recommendBody">
      <div class="card1">
        <img :src="randomPoster">
      </div>
      <div class="card2">
        <img :src="randomPoster">
      </div>
      <div class="card3">
        <img :src="randomPoster">
      </div>
      <div class="card4">
        <img :src="randomPoster">
      </div>
      <div class="card5">
        <img :src="randomPoster">
      </div>
      <div class="card6">
        <img :src="randomPoster">
      </div>
    </section>
  </div>
</template>


<script>
export default {
  name: 'RecommendView',
  computed: {
    randomPoster() {
      return `https://www.themoviedb.org/t/p/original${this.$store.getters.randomPoster.poster_path}`
    }
  },
  data() {
    return {

    }
  },
  methods: {

  },
}
</script>

<style scoped>
.recommendBody {
  display: grid;
  grid-template-areas: "card1 . card2 . card3"
  ". . . . ."
  "card4 . card5 . card6";
}


.card1{
  grid-area: card1;
  height: 25rem;
  width: 25rem;
  border-radius: 1rem;
  overflow: hidden;
  overflow-x: hidden;
  overflow-y: hidden;
  position: relative;
}

.card2{
  grid-area: card2;
  height: 25rem;
  width: 25rem;
  border-radius: 1rem;
  overflow: hidden;
  overflow-x: hidden;
  overflow-y: hidden;
  position: relative;
}

.card3{
  grid-area: card3;
  height: 25rem;
  width: 25rem;
  border-radius: 1rem;
  overflow: hidden;
  overflow-x: hidden;
  overflow-y: hidden;
  position: relative;
}

.card4{
  grid-area: card4;
  height: 25rem;
  width: 25rem;
  border-radius: 1rem;
  overflow: hidden;
  overflow-x: hidden;
  overflow-y: hidden;
  position: relative;
}

.card5{
  grid-area: card5;
  height: 25rem;
  width: 25rem;
  border-radius: 1rem;
  overflow: hidden;
  overflow-x: hidden;
  overflow-y: hidden;
  position: relative;
}

.card6{
  grid-area: card6;
  height: 25rem;
  width: 25rem;
  border-radius: 1rem;
  overflow: hidden;
  overflow-x: hidden;
  overflow-y: hidden;
  position: relative;
}

img {
  height: 100%;
  width: 100%;
}
</style>