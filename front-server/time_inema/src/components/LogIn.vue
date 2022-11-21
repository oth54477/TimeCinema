<template>
  <section class="login-body">
    <div class="login">
      <h1>LogIn Page</h1>
      <form @submit.prevent="logIn" class="login-form">
        <input type="text" id="username" placeholder="  Username" v-model="username"><br>
  
        <input type="password" id="password" placeholder="  password" v-model="password"><br>
  
        <!-- <input type="submit" value="logIn"> -->
        <button class="btn-signup" @click="logIn">Login with Username</button>
      </form>
    </div>
  </section>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn', payload)
    }
  }
}
</script>

<style>
.login-body {
  display: flex;
  justify-content: center;
  margin-top: 0px;
  flex-direction: column;
  position: fixed;
  /* top: 3vh;
  left: 10vw;
  right: 10vw;
  bottom: 0vh; */
  top: 15vh;
  left: 25vw;
  right: 25vw;    
  bottom: 15vh;
  overflow: scroll;
  border-radius: 10px;
  background-color: #eae9e4;
  font-family: 'big-caslon'
}

.login {
  display: flex;
  position: relative;
  flex-direction: column;
  color: black;
}

.login > h1 {
  color: black;
}

.login-form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.login-form > input {
  font-size: 1rem;
  border: solid 1px #b8b8b8;
}

#username {
  width: 25vw;
  height: 5vh;
}

#password {
  width: 25vw;
  height: 5vh;
}

</style>