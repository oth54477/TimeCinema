<template>
  <section>
    <div class="crew-img" >
      <img  :src="`https://www.themoviedb.org/t/p/original${cast.profile_path}`">
      <div class="cover"><span>{{ cast.name }}</span></div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'CrewItem',
  props: {
    cast: Object,
  }
}
</script>

<style>
.crew-img {
  width: 10vw;
  height: 10vw;
  border-radius: 100px;
  background-size:cover;
  /* background-position: center; */
  position: relative;
}

.crew-img  > img {
  border-radius: 100px;
  object-fit: cover;
}
.crew-img:hover .cover {
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
  width: 10vw;
  height: 10vw;
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
  align-items: center;
}

.cover > span {
  margin-top: 5vw;
}

</style>