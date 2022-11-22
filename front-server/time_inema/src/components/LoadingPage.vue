<template>
  <div class="container">
    <div class="box">
      <div class="outter">
        <h1 class="title">Time Cinema</h1>
        <!-- <img src="@/assets/TC_logo.png"> -->
        <div class="inner">
          <!-- <div class="clock"></div> -->
          <div class="bg"></div>
        </div>
        <h1 v-if="isLoading" class="loading-h1">
          Loading
          <span></span>
          <span></span>
          <span></span>
        </h1>
        <h1 v-if="!isLoading" @click="goToTime"></h1>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'LoadingPage',
  props: {
  },
  computed: {
    isLoading() {
      return this.$store.state.isLoading
    },
  },
  methods: {
    goToTime() {
      this.$router.push({ name: 'time' })
      this.$emit('isClick', true)
    },

  }

}
</script>

<style scoped>
@import url(https://fonts.googleapis.com/css?family=Lato:300);


.container{
  text-align: center;
  /* background-color: gray; */
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 75%;
  height: 75%;
}

/* .box:nth-child(2n-1){
  background-color: rgba(0,0,0,0.05);
} */

.box{
  display: flex;
  justify-content: center;
  align-items: center;
  /* position: relative; */
  /* display: inline-block; */
  /* display: flex; */
  /* justify-content: center; */
  /* align-items: center; */
  height: 100%;
  /* width: 33.3%; */
  width: 100%;
  /*margin:0 -4px -5px -2px;*/
  transition: all .2s ease;
}

.outter {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  height: 100%;
  width: 100%;
  /* position: relative; */
}

.outter h1 {
  /* font-family: Ivy Mode,serif;
  font-style: normal; */
  /* font-weight: 600; */
  /* font-size: 2em; */
  /* height: 100px; */
  color: #eae9e4;
  /* font-size: 4vw; */
  /* font-family: "Ivy Mode",serif; */
  font-weight: 300;
}

.outter > img {
  filter: invert(98%) sepia(15%) saturate(258%) hue-rotate(6deg) brightness(103%) contrast(84%);
}

.inner {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  
}
.box2 {
  height: 100%;
  width: 100%;
}
.box h1{
  /* color: #777; */
  /* font-family:  Lato,"Helvetica Neue" ; */
  /* font-weight: 300; */
  /* position: absolute; */
  /* font-size: 20px; */
  width: 100%;
  height: 25px;
  /* text-align: center; */
  bottom: 0px;
  margin: 0;
  top:160px;
  /* background-color: #fff; */
  opacity: 1;
  text-transform: uppercase;
  transition: all .2s ease;
}
/* 
.cir {
  background-color: white;
  position: absolute;
  top: 2px;
  left: 48%;
  width: 100px;
  height: 10px;
} */

/* MEDIA QUERIES */
@media (max-width: 700px){
  .box{
    width: 50%;
  }

  .box:nth-child(2n-1){
    background-color: inherit;
  }

  .box:nth-child(4n),.box:nth-child(4n-3) {
    background-color: rgba(0,0,0,0.05);
  }

}

@media (max-width: 420px){
  .box{
    width: 100%;
  }

  .box:nth-child(4n),.box:nth-child(4n-3){
    background-color: inherit;
  }

  .box:nth-child(2n-1){
    background-color:rgba(0,0,0,0.05);
  }

}


/* -------------- Clock -------------- */

.clock{
  border-radius: 1000px;
  /* border: 10px solid #fff; */
  border: 10px solid #eae9e4;
  height: 300px;
  width: 300px;
  position: relative;

  /* top: 28%; */
  /* top: 110px; */
  /* top: -webkit-calc(50% - 43px); */
  /* top: calc(50% - 43px); */
  /* left: 35%; */
  /* left: 110px; */
  /* left: -webkit-calc(50% - 43px); */
  /* left: calc(50% - 43px); */
}
.clock:after{
  content: "";
  position: absolute;
  /* background-color: #fff; */
  background-color: #eae9e4;
  top: 2px;
  left: 48%;
  height: 150px;
  width: 4px;
  border-radius: 5px;
  -webkit-transform-origin: 50% 97%;
      transform-origin: 50% 97%;
  -webkit-animation: grdAiguille 2s linear infinite;
      animation: grdAiguille 2s linear infinite;
}

@-webkit-keyframes grdAiguille{
    0%{-webkit-transform:rotate(0deg);}
    100%{-webkit-transform:rotate(360deg);}
}

@keyframes grdAiguille{
    0%{transform:rotate(0deg);}
    100%{transform:rotate(360deg);}
}

.clock:before{
  content: "";
  position: absolute;
  /* background-color: #fff; */
  background-color: #eae9e4;
  top: 2px;
  left: 48%;
  height: 150px;
  width: 4px;
  border-radius: 5px;
  -webkit-transform-origin: 50% 94%;
      transform-origin: 50% 94%;
  -webkit-animation: ptAiguille 12s linear infinite;
      animation: ptAiguille 12s linear infinite;
}

@-webkit-keyframes ptAiguille{
    0%{-webkit-transform:rotate(0deg);}
    100%{-webkit-transform:rotate(360deg);}
}

@keyframes ptAiguille{
    0%{transform:rotate(0deg);}
    100%{transform:rotate(360deg);}
}

.bg {
  height: 145px;
  width: 298px;
  /* font-size: 50px; */
  position: relative;
  background-image: url('@/assets/TC_white.png');

}

.loading-h1 {
  font-family: futur;
  font-size: 30px !important;
}

.title {
  font-size: 5rem;
}

.loading {
  width: 100vw;
  margin-top: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.loading span {
  display: inline-block;
  width: 5px;
  height: 5px;
  background-color: gray;
  border-radius: 50%;
  animation: loading 1s linear infinite;
  background-color: #eae9e4;
}

.loading-h1 span:nth-child(1) {
  animation-delay: 0s;
}

.loading-h1 span:nth-child(2) {
  animation-delay: 0.2s;
  margin: 0px 10px
}

.loading-h1 span:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes loading {
  0%, 100% {
    opacity: 0;
    transform: scale(0.5);
  }
  50% {
    opacity: 1;
    transform: scale(1.2);
  }
}
</style>