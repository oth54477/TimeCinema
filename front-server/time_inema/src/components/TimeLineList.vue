<template>
  <section id="timeline">
    <TimeLineItem 
      v-for="itemInfo in itemInfos"
      :key="itemInfo.id"
      :itemInfo="itemInfo"
    />
  </section>
</template>

<script>
import TimeLineItem from '@/components/TimeLineItem.vue'

export default {
  name: 'TimeLineList',
  components: {
    TimeLineItem,
  },
  computed: {
    itemInfos() {
      const posters = this.$store.getters.timeLinePoster
      const itemInfos = [
        {
          id: 1,
          times: '시대극',
          title: 'period movie',
          content: '다양한 시대를 배경으로 한 영화들을 보고 싶으신가요?',
          routerName: 'period',
          posterUrl: posters.period
        },
        {
          id: 2,
          times: '1900년대 배경',
          title: 'old movie',
          content: '1990년대의 분위기를 느낄 수 있는 영화들을 보고 싶으신가요?',
          routerName: 'past',
          posterUrl: posters.past
        },
        {
          id: 3,
          times: '2000년대 배경',
          title: 'modern movie',
          content: '현재를 배경으로 한 영화들을 보고 싶으신가요?',
          routerName: 'now',
          posterUrl: posters.now
        },
        {
          id: 4,
          times: '미래 배경',
          title: 'future movie',
          content: '상상력을 자극할 수 있는 미래를 배경으로 한 영화를 보고 싶으신가요?',
          routerName: 'future',
          posterUrl: posters.future
        },
      ]
      return itemInfos
    },
  },
  data() {
    return {
      
      
    }
  },

  
}
</script>

<style scoped lang="scss">
.tl-content > h1 {
  
}
#timeline {
  display: flex;
  background-color: #031625;

  &:hover {
    .tl-item {
      width: 23.3333%;
    }
  }
}

</style>