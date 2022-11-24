<template>
  <section class="watch-user-list-body">
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
.watch-user-list-body {
  display: flex;
}
</style>