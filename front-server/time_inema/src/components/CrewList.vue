<template>
  <section>
    <h1>출연진</h1>
    <div class="crew-box">
      <CrewItem 
        v-for="cast in casts.slice(1, 4)"
        :key="cast.id"
        :cast="cast"
      />
    </div>
  </section>
</template>

<script>
import CrewItem from '@/components/CrewItem'

export default {
  name: 'CrewList',
  components : {
    CrewItem,
  },
  props: {
    casts: Array,
  },
}
</script>

<style>
.crew-box {
  display: flex;
  justify-content: space-around;
  margin: 5vh 0;
}
</style>