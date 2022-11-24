<template>
  <div id="app" >
    <div class="egg" @click="egg"></div>
    <!-- <button @click="load">load</button> -->
    <div class="success" v-if="loginCnt === 1&&isShow" @click="changeShow">
      <span>로그인 성공</span><br>
      <span>{{ user.username }}님 환영합니다.</span>
    </div>
    <MusicPlayer />
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
import MusicPlayer from '@/components/MusicPlayer'

export default {
  name: 'App',
  data() {
    return {
      isShow: true,
      eggCnt: 0,
    }
  },
  components: {
    MenuBar,
    SignupModal,
    LoginModal,
    MusicPlayer,
  },
  computed: {
    modalState() {
      return this.$store.state.modalState
    },
    loginname() {
      return this.$store.state.login
    },
    loginCnt() {
      return this.$store.state.loginCnt
    },
    user() {
      return this.$store.state.user
    }
  },
  methods: {
    start() {
      this.$store.dispatch('getTopRateMovies', 1)
      this.$store.dispatch('getUserList')
      // if (this.)
      // this.$router.push({ name: 'time' })
    },
    load() {
      this.isLoaded = !this.isLoaded
    },

    closeModal(page) {
      // this.modal = false
      this.$store.commit('POP_DOWN', page)
      // this.$store.state.modal = false
    },
    changeShow() {
      this.isShow = false
    },
    egg() {
      this.eggCnt ++
      if (this.eggCnt > 5) {
        this.$router.push({ name: 'userList' })
      }
    }


  },
  created() {
    this.start()
    
  },


}
</script>

<style>
/* @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap'); */

@font-face {
  font-family: 'futur';
  src: url('@/assets/font/futur.ttf') format('truetype');
}

@font-face {
  font-family: 'big-caslon';
  /* font-family: 'NotoSansKR'; */
  src: url('@/assets/font/big-caslon.ttf') format('truetype');
  font-style: normal;
}

@font-face {
  font-family: "big-caslon";
  src: url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap') format("woff");
  unicode-range: U+0030-0039;
  font-style: normal;
}

@font-face {
  font-family: "big-caslon";
  src: url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap') format("woff");
  unicode-range: U+AC00-U+D7A3;
  font-style: normal;
}

* {
  /* font-family: 'NotoSansKR'; */
  /* font-family: 'Noto Sans KR', sans-serif; */
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
  /* text-align: center; */
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




.success {
  background-color: black;
  opacity: 0.85;
  position: absolute;
  top: 37.5vh;
  bottom:0px;
  left:0px;
  right:0px;
  height: 25vh;
  width: 100vw;
  z-index: 990;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  animation: pop 3.5s 1 forwards;
  animation-timing-function: cubic-bezier(0, 1.15, 0.9, 0.98);
  
}

.success > span {
  font-size: 50px;
  color: #eae9e4
}




@keyframes pop {
        0% {
            opacity: 0;
            /* transform: translate3d(0, -300%, 0); */
        }

        40% {
          opacity: 0.8;
        }


        100% {
          opacity: 0;

        }
}

.egg {
  border-radius: 100px;
  position: absolute;
  top: 0px;
  right: 0px;
  cursor: pointer;
  height: 10vw;
  width: 10vw;
  z-index: 999;
}
</style>
