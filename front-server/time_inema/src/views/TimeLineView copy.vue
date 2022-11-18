<template>
  <transition name="fade">
    <div class="test">
      <section id="timeline">
        
        <div class="tl-item" @click="goToRecommend('periodDrama')">
          
          <div class="tl-bg" style="background-image: url(https://mblogthumb-phinf.pstatic.net/20150914_28/shdudtn1234_1442232589804UsVv8_JPEG/%BB%E7%B1%D8_%BF%B5%C8%AD_%C3%DF%C3%B5_BEST_10%A2%BE_%C7%D1%B1%B9%C0%C7_%B8%C5%B7%C2%C0%FB%C0%CE_%B0%FA%B0%C5_%BB%E7%B1%D8%BF%B5%C8%AD%B8%A6_%BE%CB%BE%C6%BA%B8%C0%DA_%282%29.jpg?type=w2)"></div>
          
          <div class="tl-year">
            <p class="f2 heading--sanSerif">~1800</p>
          </div>
    
          <div class="tl-content">
            <h1>Lorem ipsum dolor sit</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit.</p>
          </div>
    
        </div>
    
        <div class="tl-item" @click="goToRecommend('past')">
          
          <!-- <div class="tl-bg" style="background-image: url(https://i.ytimg.com/vi/kIxAcVIhWPE/maxresdefault.jpg)"></div> -->
          <div class="tl-bg" style="background-image: url(http://www.artinsight.co.kr/data/tmp/1708/9b9f3e8bc6eb642108955e18761e07ae_8DKxYJJRM4Ni8Bm54St7TQqt7QYFsw4B.jpg)"></div>
          <!-- <div class="tl-bg" style="background-image: url(https://butterpopcorn.kr/wp-content/uploads/2019/08/%E3%84%B4%E3%85%87%E3%84%B9%E3%84%B9.jpg)"></div> -->
          
          <div class="tl-year">
            <p class="f2 heading--sanSerif">1801~2000</p>
          </div>
    
          <div class="tl-content">
            <h1 class="f3 text--accent ttu">Vestibulum laoreet lorem</h1>
            <p>Suspendisse potenti. Sed sollicitudin eros lorem, eget accumsan risus dictum id. Maecenas dignissim ipsum vel mi rutrum egestas. Donec mauris nibh, facilisis ut hendrerit vel, fringilla sed felis. Morbi sed nisl et arcu.</p>
          </div>
    
        </div>
    
        <div class="tl-item" @click="goToRecommend('now')">
          
          <div class="tl-bg" style="background-image: url(https://www.themoviedb.org/t/p/w500_and_h282_face/hAtRKAi24kw4wyGB2IyvmFdVGHC.jpg)"></div>
          
          <div class="tl-year">
            <p class="f2 heading--sanSerif">2001~2022</p>
          </div>
    
          <div class="tl-content">
            <h1 class="f3 text--accent ttu">Phasellus mauris elit</h1>
            <p>Mauris cursus magna at libero lobortis tempor. Suspendisse potenti. Aliquam interdum vulputate neque sit amet varius. Maecenas ac pulvinar nisi. Fusce vitae nunc ultrices, tristique dolor at, porttitor dolor. Etiam id cursus arcu, in dapibus nibh. Pellentesque non porta leo. Nulla eros odio, egestas quis efficitur vel, pretium sed.</p>
          </div>
    
        </div>
    
        <div class="tl-item" @click="goToRecommend('future')">
          
          <div class="tl-bg" style="background-image: url(https://upload.wikimedia.org/wikipedia/ko/f/f2/%EC%96%B4%EB%B2%A4%EC%A0%B8%EC%8A%A4-_%EC%97%94%EB%93%9C%EA%B2%8C%EC%9E%84_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg)"></div>
          
          <div class="tl-year">
            <p class="f2 heading--sanSerif">2023~</p>
          </div>
    
          <div class="tl-content">
            <h1 class="f3 text--accent ttu">Mauris vitae nunc elem</h1>
            <p>Suspendisse ac mi at dolor sodales faucibus. Nunc sagittis ornare purus non euismod. Donec vestibulum efficitur tortor, eget efficitur enim facilisis consequat. Vivamus laoreet laoreet elit. Ut ut varius metus, bibendum imperdiet ex. Curabitur diam quam, blandit at risus nec, pulvinar porttitor lorem. Pellentesque dolor elit.</p>
          </div>
    
        </div>
      </section>
  
    </div>
    
  </transition>
</template>

<script>
export default {
  name: 'TimeLineView_copy',
  methods: {
    goToRecommend(decade) {
      this.$router.push({ name: 'recommend', params: { decade: decade } })
    }
  }
}
</script>

<style scoped lang="scss">
body {
  font-family: 'Source Sans Pro',Helvetica Neue,Helvetica,Arial,sans-serif; 
  font-size: 16px;
  line-height: 1.75;
}

.test {
  position: fixed;
  top: 0px;
  left: 0px;
  transition: transform 1s cubic-bezier(0.76, 0, 0.11, 1.1);
}

.fade-enter-active {
  transition: opacity 3s ease-out;
}

#timeline {
  display: flex;
  background-color: #031625;

  &:hover {
    .tl-item {
      width: 23.3333%;
    }
  }
}



.tl-item {
  transform: translate3d(0, 0, 0);
  position: relative;
  width: 25%;
  height: 100vh;
  min-height: 600px;
  color: #fff;
  overflow: hidden;
  transition: width 0.5s ease;
  z-index: 3;
  
  &:before, &:after {
    transform: translate3d(0, 0, 0);
    content: '';
    position: absolute;
    left: 0; top: 0;
    width: 100%; height: 100%;
  }

  &:after {
    background: transparentize(#031625, 0.15);
    opacity: 1;
    transition: opacity 0.5s ease;
  }

  &:before {
    background: linear-gradient(to bottom, rgba(0,0,0,0) 0%,rgba(0,0,0,1) 75%);
    z-index: 1;
    opacity: 0;
    transform: translate3d(0, 0, 0) translateY(50%);
    transition: opacity 0.5s ease, transform 0.5s ease;
  }

  &:hover {
    width: 30% !important;
    
    &:after {
      opacity: 0;
    }

    &:before {
      opacity: 1;
      transform: translate3d(0, 0, 0) translateY(0);
      transition: opacity 1s ease, transform 1s ease 0.25s;
    }
    
    .tl-content {
      opacity: 1;
      transform: translateY(0);
      transition: all 0.75s ease 0.5s;
    }

    .tl-bg {
      filter: grayscale(0);
    }
  }
}

.tl-content {
  transform: translate3d(0, 0, 0) translateY(25px);
  position: relative;
  z-index: 1;
  text-align: center;
  margin: 0 1.618em;
  top: 55%;
  opacity: 0;
  
  h1 {
    font-family: 'Pathway Gothic One',Helvetica Neue,Helvetica,Arial,sans-serif;
    text-transform: uppercase;
    color: #1779cf;
    font-size: 1.44rem;
    font-weight: normal;
  }
}

.tl-year {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translateX(-50%) translateY(-50%);
  z-index: 1;
  border-top: 1px solid #fff;
  border-bottom: 1px solid #fff;
  
  p {
    font-family: 'Pathway Gothic One',Helvetica Neue,Helvetica,Arial,sans-serif;
    font-size: 1.728rem;
    line-height: 0;
  }
}

.tl-bg {
  transform: translate3d(0, 0, 0);
  position: absolute;
  width: 100%; height: 100%;
  top: 0; left: 0;
  background-size: cover;
  background-position: center center;
  transition: filter 0.5s ease;
  filter: grayscale(100%);
}

.tl-bg::before {
  content: "";
  position: fixed;
  background-image: url('https://www.cinecasero.uy/img/old.webp');
  background-repeat: repeat;

  opacity: 0.1;
  top: 0px;
  left: 0px;
  right: 0px;
  bottom: 0px;
  
}

</style>