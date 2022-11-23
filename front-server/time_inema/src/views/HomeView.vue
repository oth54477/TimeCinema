<template>
  <section class="home-body" @click="goToTime">
    <div class="bigBox" v-if="isCircle"  @mousemove="mouseCircle">
      <!-- <div class="film"> -->
        <!-- <img src="@/assets/sungbin.png" style="color:white"> -->
        <!-- <img src="https://www.cinecasero.uy/img/tape.png" style="color:white"> -->
      <!-- </div> -->
      <!-- <div class="film"> -->
        <!-- <img src="@/assets/sungbin.png" style="color:white"> -->
      <!-- </div> -->

        <div :class="{ 'tape-box': cnt > 1, 'tape-box-delay': cnt <= 1}">
          <div class="tape -left"></div>
          <div class="tape -right"></div>
        </div>
        <!-- <div class="tape-box2">
          <div class="tape -left"></div>
          <div class="tape -right"></div>
        </div> -->
      
    <!-- <div class="bigBox" v-if="isLoading"> -->  
      <div class="circle" v-if="!isLoading&&isCircle"  @click="clicked"><span>click</span></div>
      <LoadingPage class="loading"  @isClick="clicked" v-if="cnt <= 1"/>
    </div>
  </section>
</template>

<script>
import LoadingPage from '@/components/LoadingPage'


export default {
  name: 'HomeView',
  components: {
    LoadingPage,
  },
  computed: {
    isLoading() {
      return this.$store.state.isLoading
    },
  },
  data() {
    return {
      cnt: 0,
      isClick: false,
      isCircle: true,
    }
  },
  methods: {
    clicked() {
      this.isClick = true
    },
    goToTime() {
      if (!this.$store.state.token) {
        this.$store.commit('POP_UP', 'login')
      } else {
        if (location.pathname === '/') {
          this.isCircle = false
          this.$router.push({ name: 'time' })
          this.$emit('isClick', true)
        }
      }
    },
    mouseCircle(event) {
      const now = window.location.pathname
      if (now === '/' && !this.isLoading) {
        const circle = document.querySelector(".circle");
        const mouseX = event.clientX;
        const mouseY = event.clientY;
        circle.style.left = mouseX + 'px';
        circle.style.top = mouseY + 'px';
      }
    },
  },
  watch: {
    isLoading() {
      this.cnt += 1
      // if (this.cnt === 2) {
        // this.$router.push({ name: 'time' })
        // this.cnt = 0
      // }
    }
  },
}

</script>

<style>
.home-body {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden
}

.tape-box {
  position: relative;
  height: 100vh;
  width: 100%;
  top: 0px;
  left: 0px;
  right: 0px;
  bottom: 0px;
  animation: fadeInDown 70s infinite;
}

.tape-box-delay {
  position: relative;
  height: 100vh;
  width: 100%;
  top: 0px;
  left: 0px;
  right: 0px;
  bottom: 0px;
  animation: fadeInDown 70s 2.5s infinite;
}


@keyframes fadeInDown {
        0% {
            opacity: 1;
            transform: translate3d(0, -300%, 0);
        }
        to {
            opacity: 1;
            /* transform: translateZ(-100%); */
            transform: translate3d(0, 0, 0)
        }
}



.tape.-left {
  left: 2rem;
}

.tape.-right {
  right: 2rem;
}

.tape {
  position: absolute;
  background-image: url('@/assets/tape.png');
  background-repeat: repeat-y;
  background-size: contain;
  background-position: top center;
  height: 6872px;
  top: 0;
  width: 70px;
}
</style>