<template>
  <div id="app"  @mousemove="mouseCircle">
    <!-- <button @click="load">load</button> -->


    <SignupModal v-if="modalState.signup" @close="closeModal('signup')" />
    <LoginModal v-if="modalState.login" @close="closeModal('login')" />
    <MenuBar class="menuBar"/>
    <transition name="slide-fade" mode="out-in">
      <router-view/>
    </transition>

  </div>
</template>

<script>
import MenuBar from '@/components/MenuBar'
import SignupModal from '@/components/SignupModal'
import LoginModal from '@/components/LoginModal'

export default {
  name: 'App',
  data() {
    return {

    }
  },
  components: {
    MenuBar,
    SignupModal,
    LoginModal,
  },
  computed: {
    modalState() {
      return this.$store.state.modalState
    },
  },
  methods: {
    start() {
      this.$store.dispatch('getTopRateMovies', 1)
      // if (this.)
      // this.$router.push({ name: 'time' })
    },
    load() {
      this.isLoaded = !this.isLoaded
    },

    mouseCircle(event) {
      const now = window.location.href
      if (now === 'http://localhost:8080/') {
        const circle = document.querySelector(".circle");
        const mouseX = event.clientX;
        const mouseY = event.clientY;
        circle.style.left = mouseX + 'px';
        circle.style.top = mouseY + 'px';
      }
      
    },
    closeModal(page) {
      // this.modal = false
      this.$store.commit('POP_DOWN', page)
      // this.$store.state.modal = false
    },

  },
  created() {
    this.start()
  },


}
</script>

<style>
@font-face {
  font-family: 'big-caslon';
  src: url('@/assets/font/big-caslon.ttf') format('truetype');
}

@font-face {
  font-family: 'futur';
  src: url('@/assets/font/futur.ttf') format('truetype');
}

* {
  font-family: 'big-caslon'
}


body {
  /* background-color: rgba(248, 242, 230, 100); */
  /* background-color: #1c1c1c; */
  /* background-color: #eae9e4; */
  /* background-image: url('https://www.cinecasero.uy/img/old.webp'); */
  
  height: 100%;
  min-height: 100vh;
  position: relative;
  margin: 0px;
  -ms-overflow-style: none;
  font-family: 'big-caslon'
}

::-webkit-scrollbar {
    display: none;
  }

/* body::after {
  content: "";
  position: fixed;
  background-image: url('https://www.cinecasero.uy/img/noise-full.png');
  background-repeat: repeat;

  opacity: 0.1;
  top: 0px;
  left: 0px;
  right: 0px;
  bottom: 0px;
} */

body::before {
  content: "";
  position: fixed;
  background-image: url('https://www.cinecasero.uy/img/noise-full.png');
  /* background-repeat: repeat; */

  opacity: 0.025;
  top: 0px;
  left: 0px;
  right: 0px;
  bottom: 0px;
}

#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* display: grid; */
  /* grid-template-areas: ""; */
  position: relative;
  background-color: #1c1c1c;

  
} 

#app::before {
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





.bigBox {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  top: 0px;
  left: 0px;
  width: 100%;
  height: 100%;
  min-height: 100vh;
  /* font-family: ivymode, sans-serif; */
  font-style: normal;
  font-weight: 600;
  /* font-size: 2em; */

  cursor: pointer;

}

.loading {
  width: 300px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  /* top: 500px;
  left: 1200px; */
}

/* .loading {
  width: 300px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
} */

/* .loading {
  position: absolute;
  width: 300px;
  top:0;right:0;bottom:0;left:0;
  display: -webkit-box;
  display: -moz-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
  align-items: center;
  justify-content: center;
  -webkit-align-items: center;
  -webkit-justify-content: center;
  -webkit-box-pack: center;
  -webkit-box-align: center;
  -moz-box-pack: center;
  -moz-box-align: center;
  -ms-box-pack: center;
  -ms-box-align: center;
} */

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.fade-enter {
  opacity: 0;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease-out;
}

.fade-leave-to {
  opacity: 0;
}

.slide-fade-enter {
  transform: translateX(10px);
  opacity: 0;
}

.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 1s ease;
}

.slide-fade-leave-to {
  transform: translateX(-10px);
  opacity: 0;
}

.circle { 
  --size: 75px;
  display: block;
  position: fixed;
  z-index: 9999;
  top: 0;
  left: 0;
  pointer-events: none;
  will-change: transform;
  mix-blend-mode: difference;
  cursor: pointer;
}

.circle span {
    border-radius: 50%;
    width: var(--size);
    height: var(--size);
    left: calc(var(--size)/-2);
    top: calc(var(--size)/-2);
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    text-transform: uppercase;
    background-color: #eae9e4;
    color: #1c1c1c;
    cursor: pointer;
    font-size: 20px;
}
/* .circle { 
  position: absolute;
  top: 0;
  left: 0; 
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background-color: #eae9e4;
  transform: translate(-50%, -50%); 
  cursor: pointer;
} */

.film:nth-child(1) {
  /* max-width: 100px; */
  /* overflow: hidden; */
  /* height: 100%; */
  /* width: 100%; */
  position: absolute;
  top: 0px;
  left: 0px;
  color: #1c1c1c;
  /* display: flex; */
  /* justify-content: space-between; */
}


.film:nth-child(2) {
  /* max-width: 100px; */
  /* overflow: hidden; */
  /* height: 100%; */
  /* width: 100%; */
  position: absolute;
  top: 0px;
  right: 0px;
  color: #1c1c1c;
  /* display: flex; */
  /* justify-content: space-between; */
}



.film > img {
  mask-image: white;
}





</style>
