<template>
  <section>
    <div class="login">
      <h1>LogIn Page</h1>
      <form @submit.prevent="logIn">
        <label for="username">username : </label>
        <input type="text" id="username" v-model="username"><br>
  
        <label for="password"> password : </label>
        <input type="password" id="password" v-model="password"><br>
  
        <input type="submit" value="logIn">
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
.login {
  display: flex;
  position: relative;
  flex-direction: column;
  color: antiquewhite;
}
</style>