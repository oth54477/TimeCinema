import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import _ from 'lodash'
// import router from '@/router'
import createPersistedState from 'vuex-persistedstate'

import SERVER from '@/api/drf.js'

Vue.use(Vuex)


const TMDB_API_KEY = process.env.VUE_APP_TMDB_API_KEY
const TMDB_API_URL = process.env.VUE_APP_TMDB_API_URL
const DJANGO_API_URL = SERVER.URL
console.log(TMDB_API_URL)
// const TMDB_API_URL = "https://api.themoviedb.org/3/movie"
// const DJANGO_API_URL = "http://127.0.0.1:8000"
// const DJANGO_API_URL = "http://192.168.212.86:8000"
// const DJANGO_API_URL = process.env.VUE_APP_DJANGO_API_URL

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      paths: ['token', 'user', 'movies', 'userList']
    })
  ],
  state: {
    token: null,
    user: {
      id: null,
      username: null,
    },
    login: null,
    loginCnt: 0,
    movies: null,
    isLoading: false,
    modal: false,
    userList: null,
    timesTable: {
      period: 0,
      past: 1,
      now: 2,
      future: 3,
    },
    trailers: null,
    modalState: {
      signup: false,
      login: false,
      profile: false,
    },
    OSTs: [
    ]
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
    },
    userInfo(state, user) {
      return user
    },

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
      }, 2500)
    },
    // 회원가입 && 로그인
    SAVE_TOKEN(state, payload) {
      console.log('token', payload.token)
      state.token = payload.token
      state.loginCnt ++
      // router.push({ name: 'ArticleView' })
      // router.push({ name: 'time' })
      // this.$store.commit('POP_DOWN', 'login')
      state.modalState.login = false
      state.modalState.signup = false
      state.login = payload.username
      this.dispatch('getUserProfile')
    },
    LOG_OUT(state) {
      state.token  = null
      console.log('로그아웃!!')
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
    },
    GET_USER_LIST(state, userList) {
      state.userList = userList
    },
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
        url: `${DJANGO_API_URL}/movies/movie_list`,
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
      axios.post(`${DJANGO_API_URL}/accounts/signup/`, payload, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
        .then((res) => {
          console.log(res)
          context.commit('SAVE_TOKEN', {token: res.data.key, username: payload.username})
        })
        .catch((error => {
          console.log(error)
        }))
    // signUp(context, payload) {
    //   axios({
    //     method: 'post',
    //     url: `${DJANGO_API_URL}/accounts/signup/`,
    //     data: {
    //       username: payload.username,
    //       password1: payload.password1,
    //       password2: payload.password2,
    //       profile_image: payload.profile_image
    //     }
    //   })
    //     .then((res) => {
    //       console.log(res)
    //       context.commit('SAVE_TOKEN', {token: res.data.key, username: payload.username})
    //     })
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
          console.log(res.config.data)
          context.commit('SAVE_TOKEN', {token: res.data.key, username: payload.username})
        })
        .catch((error) => {
          console.log('로그인 실패',error)
          window.alert("로그인에 실패했습니다!")
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
          if (trailers.length === 0) {
            axios({
              method: 'get',
              url: `${TMDB_API_URL}/${payload.id}/videos`,
              params: {
                      api_key: TMDB_API_KEY,
                      language: 'en-US',
                      },  
            })
              .then((res) => {
                console.log('영어예고편 -> ',res)
                const trailers = res.data.results

                let payload = []
                trailers.forEach(trailer => payload.push({
                  titl: trailer.name,
                  url: trailer.key,
                }))
      
                context.commit('GET_TRAILER', payload)
              })
          } else {
            let payload = []
            trailers.forEach(trailer => payload.push({
              titl: trailer.name,
              url: trailer.key,
            }))
  
            context.commit('GET_TRAILER', payload)
          }

        })
    },
    getUserProfile(context) {
      axios({
        method: 'get',
        url: `${DJANGO_API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${context.state.token}` 
        }
      })
        .then((res) => {
          // console.log('유저',res)
          // context.getters.userInfo(res.data)
          context.state.user.id = res.data.pk
          context.state.user.username = res.data.username
        })
      // console.log('테스트', this.res)
    },
    getUserList(context) {
      axios({
        method: 'get',
        url: `${DJANGO_API_URL}/movies/user_list`,
      })
        .then((res) => {
          context.commit('GET_USER_LIST', res.data)
        })
    }

    
  },
  modules: {
  }
})

