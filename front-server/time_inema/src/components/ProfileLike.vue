<template>
  <section class="profile-like=body">
    <div class="profile-like">
      <div class="like-img" :style="{backgroundImage: `url(https://www.themoviedb.org/t/p/original${like.poster_path})`}"></div>
      <!-- <img class="like-img" :src="`https://www.themoviedb.org/t/p/original${like.poster_path}`"> -->
    </div>
  </section>
</template>

<script>
export default {
  name: 'ProfileLike',
  components: {
    
  },
  props: {
    like: Object,
  }
}
</script>

<style>
.like-img {
  width: 10vw;
  height: 23vh;
  border-radius: 10px;
  margin: 5px 5px;
  background-size: cover;
}
</style>