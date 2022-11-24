<template>
  <transition name="fade">
    <div class="test">
      <TimeLineList />
    </div>
    
  </transition>
</template>

<script>
import TimeLineList from '@/components/TimeLineList'

export default {
  name: 'TimeLineView',
  components: {
    TimeLineList,
  },
  computed: {

  },
  methods: {

  }
}
</script>

<style scoped lang="scss">
// body {
//   font-family: 'Source Sans Pro',Helvetica Neue,Helvetica,Arial,sans-serif; 
//   font-size: 16px;
//   line-height: 1.75;
// }

.test {
  position: fixed;
  top: 0px;
  left: 0px;
  transition: transform 1s cubic-bezier(0.76, 0, 0.11, 1.1);
  background-color: #1c1c1c;
  width: 100vw;
}

.fade-enter-active {
  transition: opacity 3s ease-out;
}
</style>