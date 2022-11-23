<template>
  <section>
    <WatchUserItem 
      v-for="watchUser in watchUsers"
      :key="watchUser.id"
      :watchUser = watchUser
    />
  </section>
</template>

<script>
import WatchUserItem from '@/components/WatchUserItem'

export default {
  name: 'WatchUserList',
  components: {
    WatchUserItem,
  },
  props: {
    watchUsers: Array,
  }
}
</script>

<style>

</style>