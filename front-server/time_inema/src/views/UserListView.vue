<template>
  <section class="user-list-body">
    <div class="user-list">
      <div style="text-align:center"><h1>🎈회원님들🎈</h1></div>
        <UserListItem 
          v-for="user in userList"
          :key="user.id"
          :user="user"
        />
    </div>
  </section>
</template>

<script>
import UserListItem from '@/components/UserListItem'
import axios from 'axios'
import SERVER from '@/api/drf.js'

const DJANGO_API_URL = SERVER.URL

export default {
  name: 'UserListView',
  components: {
    UserListItem,
  },
  data() {
    return {
      userList: null
    }
  },
  created() {
    axios({
      method: 'get',
      // url: `http://192.168.212.86:8000/movies/user_list`
      url: `${DJANGO_API_URL}/movies/user_list`
    })
      .then((res) => {
        console.log(res.data)
        this.userList = res.data
      })
  }
}
</script>

<style>
.user-list-body {
  overflow: scroll;
}

.user-list {
  display: flex;
  /* justify-content: center; */
  margin-top: 0px;
  flex-direction: column;
  position: fixed;
  /* top: 3vh;
  left: 10vw;
  right: 10vw;
  bottom: 0vh; */
  top: 10vh;
  left: 20vw;
  right: 20vw;
  bottom: 10vh;
  overflow: scroll;
  border-radius: 10px;
  background-color: #eae9e4;
  color: #1f1f1f;
}

.user-list {
  padding: 5vw 5vh;
}

</style>