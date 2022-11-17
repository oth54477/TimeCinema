<template>
  <div>
    <div class="timeBox">
      <div class="yearbox">1</div>
      <div class="yearbox">2</div>

    </div>
  </div>
</template>

<script>
export default {
  name: 'TimeLineView2',
  components: { 

  },
  computed: {
    
  },
  data() {
    return {

    }
  },
  methods: {

  },
}
</script>

<style scoped lang="scss">
.timeBox {
  position: relative;
  top: 0px;
  left: 0px;
  width: 100%;
  height: 100%;
  min-height: 100vh;

}

.timeBox:before{
  content: "";
  position: absolute;
  background-color: #4557bb;
  top: 0px;
  left: 10%;
  height: 100%;
  width: 4px;
  border-radius: 5px;
  -webkit-transform-origin: 50% 97%;
      transform-origin: 50% 97%;
  -webkit-animation: grdAiguille 2s linear infinite;
      animation: grdAiguille 2s linear infinite;
}

.yearbox {
  border: 3px solid #00127a;
  margin: 10px;
  width: 100px;
  height: 100px;
  background-color: #4557bb;
}
</style>