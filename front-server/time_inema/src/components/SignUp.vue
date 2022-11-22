<template>
  <section class="signup-body">
    <div class="signup">
      <h1>Join Cinema Time</h1>
      <form class="signup-form" @submit.prevent="signUp">
        <input type="text" id="username" placeholder="  Username" v-model="username"><br>
        <input type="password" id="password1" placeholder="  Password" v-model="password1"><br>
        <input type="password" id="password2" placeholder="  Password confirmation" v-model="password2">
        <button class="btn-signup" @click="signUp">Join with Username</button>
        <div class="or">
          <hr>
          <h2 style="color:black;">or</h2>
          <hr>
        </div>
        <button class="btn-google">Join with Google</button>
        <!-- <input class="btn-signup" type="submit" value="SignUp"> -->
      </form>
    </div>
    <div class="signup-foot">
      <div class="go-to-login">
        <h1>Already have an account?</h1>
        <h1  @click="goToLogin"> Log in</h1>
      </div>
      <div class="foot">
        <p class="signup-content">By joining Time cinema, You agree to our Terms of Service, Privacy Plicy and Cookis Policy.</p>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'SignUp',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        // username,
        // password1,
        // password2,
        username: username,
        password1: password1,
        password2: password2, 
        profile_image: '@/assets/smaple_profile.png',
      }

      this.$store.dispatch('signUp', payload)
      this.$store.commit('POP_DOWN', 'signup')

    },
    goToLogin() {
      this.$store.commit('POP_DOWN', 'signup')
      this.$store.commit('POP_UP', 'login')
    }
  }
}
</script>

<style>
.signup-body {
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

.signup {
  display: flex;
  position: relative;
  flex-direction: column;
  color: black;
}

.signup > h1 {
  color: black;
}

.signup-form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.signup-form > input {
  font-size: 1rem;
  border: solid 1px #b8b8b8;
}

#username {
  width: 25vw;
  height: 5vh;
}

#password1 {
  width: 25vw;
  height: 5vh;
}

#password2 {
  width: 25vw;
  height: 5vh;
}

.btn-signup {
  width: 25vw;
  height: 5vh;
  margin-top: 2.5vh;
  cursor: pointer;
  color: white;
  font-size: 1.2rem;
  font: bolder;
  font-weight: 600;
  background-color: #b8b8b8;
  border: none;
}

.btn-google {
  width: 25vw;
  height: 5vh;
  /* margin-top: 2.5vh; */
  cursor: pointer;
  color: #b8b8b8;
  font-size: 1.2rem;
  font: bolder;
  font-weight: 600;
  background-color: white;
  border: none;
}

.go-to-login {
  display: flex;
  justify-content: center;
} 

.go-to-login > h1 {
  margin: 20px 10px;
}

.go-to-login > h1:nth-child(2) {
  font-style: italic;
  cursor: pointer;

}

.signup-content {
  width: 25vw;
}

.signup-foot {
  display: flex;
  flex-direction: column;
}

.foot {
  display: flex;
  justify-content: center;
}

hr {
  height: 0vh;
  width: 10vw;
  background-color: black;
  border: solid 1.5px black;
  margin: 0px 1vw;
}

.or {
  display: flex;
  justify-content: center;
  align-items: center;
}

</style>