<template>
  <section class="user-list-item">
    <h2>{{ user.id }}번째 회원</h2>
    <div class="userr">
      <img class="user-list-img" :src="`http://192.168.212.86:8000${user?.profile_image}`" alt="">
      <div>
        <h2>{{ user.username }}</h2>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'UserListItem',
  props: {
    user:Object,
  },
}
</script>

<style>
.user-list-item {
}

.user-list-img {
  height: 10vw;
  width: 10vw;
  border-radius: 100px;
}

.userr {
  display: flex;

}
</style>