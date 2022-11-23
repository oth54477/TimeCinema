<template>
  <div class="tl-item" @click="goToRecommend(itemInfo.routerName)">
    <!-- <div class="tl-bg" style="background-image: url(https://mblogthumb-phinf.pstatic.net/20150914_28/shdudtn1234_1442232589804UsVv8_JPEG/%BB%E7%B1%D8_%BF%B5%C8%AD_%C3%DF%C3%B5_BEST_10%A2%BE_%C7%D1%B1%B9%C0%C7_%B8%C5%B7%C2%C0%FB%C0%CE_%B0%FA%B0%C5_%BB%E7%B1%D8%BF%B5%C8%AD%B8%A6_%BE%CB%BE%C6%BA%B8%C0%DA_%282%29.jpg?type=w2)"></div> -->
    <div class="tl-bg" :style="posterObject"></div>
    <div class="tl-year">
      <p class="f2 heading--sanSerif">{{ itemInfo.times }}</p>
    </div>

    <div class="tl-content">
      <h1>{{ itemInfo.title }}</h1>
      <p>{{ itemInfo.content }}</p>
    </div>

  </div>
</template>

<script>
export default {
  name: 'TimeLineItem',
  computed: {
    posterObject() {
      return {
        backgroundImage: `url(https://www.themoviedb.org/t/p/original${this.itemInfo.posterUrl?.poster_path})`
      }
    }
  },
  props: {
    itemInfo: Object,
  },  
  methods: {
    goToRecommend(times) {
      this.$router.push({ name: 'recommend', params: { times: times } })
    }
  }
  
  
}
</script>

<style scoped lang="scss">

.tl-item {
  transform: translate3d(0, 0, 0);
  position: relative;
  width: 25%;
  height: 100vh;
  min-height: 600px;
  color: #fff;
  overflow: hidden;
  transition: width 0.5s ease;
  z-index: 3;
  
  &:before, &:after {
    transform: translate3d(0, 0, 0);
    content: '';
    position: absolute;
    left: 0; top: 0;
    width: 100%; height: 100%;
  }

  &:after {
    background: transparentize(#031625, 0.15);
    opacity: 1;
    transition: opacity 0.5s ease;
  }

  &:before {
    background: linear-gradient(to bottom, rgba(0,0,0,0) 0%,rgba(0,0,0,1) 75%);
    z-index: 1;
    opacity: 0;
    transform: translate3d(0, 0, 0) translateY(50%);
    transition: opacity 0.5s ease, transform 0.5s ease;
  }

  &:hover {
    width: 30% !important;
    
    &:after {
      opacity: 0;
    }

    &:before {
      opacity: 1;
      transform: translate3d(0, 0, 0) translateY(0);
      transition: opacity 1s ease, transform 1s ease 0.25s;
    }
    
    .tl-content {
      opacity: 1;
      transform: translateY(0);
      transition: all 0.75s ease 0.5s;
    }

    .tl-bg {
      filter: grayscale(0);
    }
  }
}

.tl-content {
  transform: translate3d(0, 0, 0) translateY(25px);
  position: relative;
  z-index: 1;
  text-align: center;
  margin: 0 1.618em;
  top: 55%;
  opacity: 0;
  
  h1 {
    // font-family: 'Pathway Gothic One',Helvetica Neue,Helvetica,Arial,sans-serif;
    text-transform: uppercase;
    color: #1779cf;
    font-size: 1.44rem;
    font-weight: normal;
  }
}

.tl-year {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translateX(-50%) translateY(-50%);
  z-index: 1;
  border-top: 1px solid #fff;
  border-bottom: 1px solid #fff;
  
  p {
    // font-family: 'Pathway Gothic One',Helvetica Neue,Helvetica,Arial,sans-serif;
    font-size: 1.728rem;
    line-height: 0;
  }
}

.tl-bg {
  transform: translate3d(0, 0, 0);
  position: absolute;
  width: 100%; height: 100%;
  top: 0; left: 0;
  background-size: cover;
  background-position: center center;
  transition: filter 0.5s ease;
  filter: grayscale(100%);
}

.tl-bg::before {
  content: "";
  position: fixed;
  background-image: url('https://www.cinecasero.uy/img/old.webp');
  background-repeat: repeat;

  opacity: 0.1;
  top: 0px;
  left: 0px;
  right: 0px;
  bottom: 0px;
  
}
</style>