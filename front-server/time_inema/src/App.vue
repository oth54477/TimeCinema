<template>
  <div id="app">
    <!-- <button @click="load">load</button> -->
    
    <div class="bigBox" v-if="isLoading">
      <LoadingPage class="loading" />
    </div>
    <MenuBar class="menuBar"/>
    <router-view/>
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
  background-color: rgba(248, 242, 230, 100);
  height: 100%;
  min-height: 100vh;
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





.bigBox {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  top: 0px;
  left: 0px;
  width: 100%;
  height: 100%;
  min-height: 100vh;
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
</style>
