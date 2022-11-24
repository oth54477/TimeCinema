<template>
  <section class="user-img" >
    <img :src="`${DJANGO_API_URL}${watchUser.profile_image}`">
    <div class="cover"><span>{{ watchUser.username }}</span></div>
  </section>
</template>

<script>
import SERVER from '@/api/drf.js'


export default {
  name: 'WatchUserItem',
  props: {
    watchUser: Object,
  },
  computed: {
   DJANGO_API_URL() {
      return SERVER.URL
    }
  }
}
</script>

<style scoped>
.user-img {
  width: 3vw;
  height: 3vw;
  border-radius: 100px;
  background-size:cover;
  position: relative;
  margin: 0px 0.3vw;
}

.user-img  > img {
  border-radius: 100px;
  object-fit: cover;
  z-index: 30;
}

.user-img:hover .cover {
  animation: info 1.5s forwards ;
}

@keyframes info {
  0% {

  }
  100% {
    opacity: 1;
  }
}

.cover {
  width: 3vw;
  height: 3vw;
  border-radius: 100px;

  /* background-color: black; */
  background: linear-gradient(180deg, #0000003d, #201f1f);;
  position: absolute;
  top: 0px;
  left: 0px;
  opacity: 0;
  z-index: 50;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: flex-end;
}

.cover > span {
  margin-top: 5vw;
  margin-bottom: 0.7vw;
  font-size: 15px;;
}
</style>