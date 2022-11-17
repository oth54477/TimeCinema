<template>
  <VueSlickCarousel v-bind="settings" class="timeLine">
      <div class="box"><h2>1</h2></div>
      <div class="box"><h2>2</h2></div>
      <div class="box"><h2>3</h2></div>
      <div class="box"><h2>4</h2></div>
      <div class="box"><h2>5</h2></div>
      <div class="box"><h2>6</h2></div>
      <div class="box"><h2>7</h2></div>
      <div class="box"><h2>8</h2></div>
  </VueSlickCarousel>
</template>

<script>
import VueSlickCarousel from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
  // optional style for arrows & dots
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'

export default {
  name: 'TimeLineView2',
  components: { VueSlickCarousel },
  computed: {
    
  },
  data() {
    return {
      settings: {
        "dots": true,
        "focusOnSelect": true,
        "infinite": true,
        "speed": 500,
        "slidesToShow": 3,
        "slidesToScroll": 3,
        "touchThreshold": 5
      }
    }
  },
  methods: {

  },
}
</script>

<style scoped>
.timeLine {
  width: 100%;
  height: 1000px;
  display: flex;
  /* justify-content: space-around; */
  align-items: center;
}

.box {
  background-color: green;
  /* width: 10px; */
  /* height: 300px; */
  margin: 10px;
}
</style>