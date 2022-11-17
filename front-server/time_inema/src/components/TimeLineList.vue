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
          times: '~1800',
          title: 'period movie',
          content: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit.',
          routerName: 'period',
          posterUrl: posters.period
        },
        {
          id: 2,
          times: '1801~2000',
          title: 'old movie',
          content: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit.',
          routerName: 'past',
          posterUrl: posters.past
        },
        {
          id: 3,
          times: '2001~2022',
          title: 'modern movie',
          content: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit.',
          routerName: 'now',
          posterUrl: posters.now
        },
        {
          id: 4,
          times: '2023~',
          title: 'future movie',
          content: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit.',
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