<template>
  <section class="music-player-body">
    <div class="fa fa-solid fa-headphones audio-btn" @click="toggleAudio"></div>
    <!-- <audio src="../assets/music/A Lovely Night-라라랜드.mp3" autoplay loop controls id="myAudio">오디오 지원되지 않는 브라우저</audio> -->
    <audio id="myaudio" autoplay loop controls v-show="isShow">
      <source id="main">
      <source :src="OSTs[0]">
      <source src="../assets/music/Another Day Of Sun-라라랜드.mp3">
      <source src="../assets/music/Falling Slowly-원스.mp3">
      <!-- <source src="http://upload.wikimedia.org/wikipedia/commons/3/32/C-major.ogg">
      <source src="http://upload.wikimedia.org/wikipedia/commons/4/4b/D-major.ogg"> -->
    </audio>
  </section>
</template>

<script>
export default {
  name: 'MusicPlayer',
  computed: {
    // OSTs() {
    //   return this.$store.state.OSTs
    // }
  },
  data() {
    return {
      isShow: false,
      OSTs: [
        "../assets/music/Another Day Of Sun-라라랜드.mp3"
      ]
    }
  },
  methods: {
    toggleAudio() {
      this.isShow = !this.isShow
    }
  }
}
</script>

<style>
.music-player-body {
  position: absolute;
  z-index: 999;
  right: 1vh;
  top: 1vh;
}

#myaudio {
  position: absolute;
  top: 0px;
  left: 0px;
  z-index: 999;
  top: 4vh;
  left: -13.7vw;
}

.audio-btn {
  font-size: 2rem;

}
</style>