import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import _ from 'lodash'
import router from '@/router'

Vue.use(Vuex)

const TMDB_API_KEY = process.env.VUE_APP_TMDB_API_KEY
const TMDB_API_URL = "https://api.themoviedb.org/3/movie"

const DJANGO_API_URL = "http://127.0.0.1:8000"

export default new Vuex.Store({
  state: {
    token: null,
    movies: null,
    isLoading: false,
    modal: false,
    timesTable: {
      period: 0,
      past: 1,
      now: 2,
      future: 3,
    },
    trailers: null,
    reviews: [
      {
        id: 1,
        movieId: 436270,
        userId: 1,
        score: 5,
        content: '지루하지 않고 킬링 타임으로 좋았다.'
      },
      {
        id: 2,
        movieId: 436270,
        userId: 1,
        score: 4,
        content: '액션이 시원시원하니 좋았다.'
      },
      {
        id: 3,
        movieId: 436270,
        userId: 1,
        score: 2,
        content: '지루하지 않고 킬링 타임으로 좋았다.'
      }
    ],
    userInfo: [
      {
        id: 1,
        name: '김싸피',
        img: 'https://www.freeiconspng.com/thumbs/profile-icon-png/profile-icon-9.png'
      }
    ],
    modalState: {
      signup: false,
      login: false,
    },
  },
  getters: {
    wait(sec) {
      let start = Date.now(), now = start;
      while (now - start < sec * 1000) {
          now = Date.now();
      }
    },
    timeLinePoster(state) {
      const movies = state.movies
      const posters = {
        period: _.sample(movies[0]),
        past: _.sample(movies[1]),
        now: _.sample(movies[2]),
        future: _.sample(movies[3]),
      }
      return posters
    },
    randomPoster(state) {
      const movies = state.movies
      return movies

    },
    movieDetail: (state) => (payload) => {
      const idx = state.timesTable[payload.times]
      const movies =state.movies[idx]
      console.log('movies!!', movies)
      const movie = movies.find(movie => movie.movie_id === payload.id)
      console.log('movie!!', movie)
      return movie
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
      }, 1000)
    },
    // 회원가입 && 로그인
    SAVE_TOKEN(state, token) {
      console.log('token',token)
      state.token = token
      // router.push({ name: 'ArticleView' })
      router.push({ name: 'time' })
    },
    MODAL(state, status) {
      state.modal = status
    },
    GET_TRAILER(state, trailers) {
      state.trailers = trailers
    },
    POP_UP(state, page) {
      state.modalState[page] = true
    },
    POP_DOWN(state, page) {
      state.modalState[page] = false
    }
  },
  actions: {
    // getTopRateMovies(context, page) {
    //   context.commit('LOADING_START')
    //   axios({
    //     method: 'get',
    //     url: TMDB_API_URL,
    //     params: {
    //       api_key: TMDB_API_KEY,
    //       language: 'ko-KR',
    //       page: page
    //     },
    //   })
    //     .then((response) => {
    //       console.log(response)
    //       const movies = response.data.results
    //       console.log(movies)
    //       context.commit('GET_TOP_RATE_MOVIES', movies)
    //     })
    //     .catch((error) => {
    //       console.log(error)
    //     })
    getTopRateMovies(context) {
      context.commit('LOADING_START')
      axios({
        method: 'get',
        url: `${DJANGO_API_URL}/movies/movie_list/`,
      })
        .then((response) => {
          console.log(response)
          const movies = response.data
          console.log(movies)
          context.commit('GET_TOP_RATE_MOVIES', movies)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${DJANGO_API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${DJANGO_API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then((res) => {
          console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
    },
    getTrailer(context, payload) {
      axios({
        method: 'get',
        url: `${TMDB_API_URL}/${payload.id}/videos`,
        params: {
                api_key: TMDB_API_KEY,
                language: 'ko-KR',
                },      
      })
        .then((res) => {
          console.log('예고편 -> ',res)
          const trailers = res.data.results
          let payload = []
          trailers.forEach(trailer => payload.push({
            titl: trailer.name,
            url: trailer.key,
          }))
          context.commit('GET_TRAILER', payload)
        })
    }
  },
  modules: {
  }
})
