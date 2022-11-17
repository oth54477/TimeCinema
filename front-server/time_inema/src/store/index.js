import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const TMDB_API_KEY = process.env.VUE_APP_TMDB_API_KEY
const TMDB_API_URL = "https://api.themoviedb.org/3/movie/top_rated"

export default new Vuex.Store({
  state: {
    movies: null,
    isLoading: false
  },
  getters: {
    wait(sec) {
      let start = Date.now(), now = start;
      while (now - start < sec * 1000) {
          now = Date.now();
      }
    }
  },
  mutations: {
    LOADING_START(state) {
      state.isLoading = true
      console.log('loading : ', state.isLoading)
    },
    GET_TOP_RATE_MOVIES(state, movies) {
      state.movies = movies
      // this.getters.wait(2)
      setTimeout(function () {
        state.isLoading = false
        console.log('loading : ', state.isLoading)
      }, 3000)
    },
  },
  actions: {
    getTopRateMovies(context, page) {
      context.commit('LOADING_START')
      axios({
        method: 'get',
        url: TMDB_API_URL,
        params: {
          api_key: TMDB_API_KEY,
          language: 'ko-KR',
          page: page
        },
      })
        .then((response) => {
          console.log(response)
          const movies = response.data.results
          console.log(movies)
          context.commit('GET_TOP_RATE_MOVIES', movies)
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
  modules: {
  }
})
