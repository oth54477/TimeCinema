<template>
  <section class="login-body">
    <div class="login">
      <h1>Log In</h1>
      <br>
      <form @submit.prevent="logIn" class="login-form">
        <input type="text" id="username" placeholder="  Username" v-model="username"><br>
  
        <input type="password" id="password" placeholder="  password" v-model="password"><br>
  
        <!-- <input type="submit" value="logIn"> -->
        <button class="btn-signup">Login with Username</button>
      </form>
      <div class="go-to-signup">
        <h1>Don't have an account?</h1>
        <h1  @click="goToSignup">Sign Up</h1>
      </div>
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
    },
    goToSignup() {
      this.$store.commit('POP_DOWN', 'login')
      this.$store.commit('POP_UP', 'signup')
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
  align-items: center;
}

.login > h1 {
  color: black;
  font-size: 40px;
  margin-bottom: 0px;
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

.go-to-signup {
  color: #2C3E50;
  display: flex;
}

.go-to-signup > h1 {
  margin: 20px 5px ;
}
</style>