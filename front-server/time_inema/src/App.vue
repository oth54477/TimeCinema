<template>
  <div id="app">
    <!-- <button @click="load">load</button> -->
    
    <div class="bigBox" v-if="isLoading">
      
      <LoadingPage class="loading" />
    </div>
    <MenuBar class="menuBar"/>
    <transition name="slide-fade" mode="out-in">
      <router-view/>
    </transition>

  </div>
</template>

<script>
import LoadingPage from '@/components/LoadingPage'
import MenuBar from '@/components/MenuBar'

export default {
  name: 'App',
  data() {
    return {
      cnt: 0
    }
  },
  components: {
    LoadingPage,
    MenuBar,
  },
  computed: {
    isLoading() {
      return this.$store.state.isLoading
    }
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
    test() {
      console.log(11)
    }
  },
  created() {
    this.start()
  },
  watch: {
    isLoading() {
      this.cnt += 1
      if (this.cnt === 2) {
        this.$router.push({ name: 'time' })
        this.cnt = 0
      }
    }
  }
}
</script>

<style>
body {
  /* background-color: rgba(248, 242, 230, 100); */
  background-color: #1c1c1c;
  /* background-color: #eae9e4; */
  /* background-image: url('https://www.cinecasero.uy/img/old.webp'); */
  
  height: 100%;
  min-height: 100vh;
  position: relative;
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
  background-repeat: repeat;

  opacity: 0.025;
  top: 0px;
  left: 0px;
  right: 0px;
  bottom: 0px;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* display: grid; */
  /* grid-template-areas: ""; */
  position: relative;
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
  font-family: ivymode, sans-serif;
  font-style: normal;
  font-weight: 600;
  font-size: 2em;
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

</style>
