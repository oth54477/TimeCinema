<template>
  <div class="container">
    <div class="menu-toggle" @click="clickMenu" :class="{ open: isClicked }">
      <span class="fa fa-plus"></span>
    </div>
    
    <div class="menu-round" :class="{ open: isClicked }">
      <div class="btn-app">
        <div class="fa fa-brands fa-github"></div>
      </div>
      <div class="btn-app">
        <div class="fa fa-facebook"></div>
      </div>
      <div class="btn-app">
        <div class="fa fa- fa-wikipedia-w"></div>
      </div>
    </div>
    
    <div class="menu-line" :class="{ open: isClicked }">
      <div class="btn-app">
        <div class="fa fa-map-marker"></div>
      </div>
      <div class="btn-app">
        <div class="fa fa-envelope"></div>
      </div>
      <div class="btn-app">
        <div class="fa fa-video-camera"></div>
      </div>
      <div class="btn-app">
        <div class="fa fa-soundcloud"></div>
      </div>
      <div class="btn-app">
        <div class="fa fa-graduation-cap"></div>
      </div>
      <div class="btn-app">
        <div class="fa fa-image"></div>
      </div>
      <div class="btn-app" @click="goToTime">
        <div class="fa fa-vine"></div>
      </div>
    </div>
    
    
  </div>
</template>

<script>
export default {
  name: 'MenuBar',
  data() {
    return {
      isClicked: false,
    }
  },
  methods: {
    clickMenu() {
      this.isClicked = !this.isClicked
    },
    goToTime() {
      this.$router.push({ name: 'time' })
      this.isClicked = !this.isClicked
    }
  },
}
</script>

<style scoped lang="scss">
// this -- well, because this.
* {
	box-sizing:border-box;
}

// this makes a basic circle
@mixin circle($param) {
	width:$param;
	height:$param;
	border-radius:50%;
}

// Brand Colour Palette
$purple:#462882;
$green:#1ef0a0;
$blue:#4644fd;
$red:#ff3c4b;

body {
	// background-color: $purple;
	background-color: gray;
	height:100vh;
	width:100vw;
	position: relative;
}

// this is what I use to place the menu thing wherever I want
.container {
	position: fixed;
	bottom:1em;
	right:1em;
}

// this toggles the whole damn thing
.menu-toggle {
	@include circle(60px);
	background-color: $green;
	box-shadow:4px 4px 2px 1px rgba(#000, 0.2);
	
	position: absolute;
	z-index:5;
	bottom:0;
	right:0;
	display:table;
	
	text-align: center;
	
	.fa {
		color:#fff;
		font-size:2em;
		display:table-cell;
		vertical-align:middle;
		transition:0.4s;
	}
	
	// Twist the plus so it looks like a close 'x'
	&.open .fa {
		transform:rotate(135deg);
	}
}

// Single Template buttons
.btn-app {
	@include circle(2.5em);
	position:absolute;
	
	background-color: $blue;
	color:#fff;
	text-align: center;
	
	.fa {
		line-height:2.5em;
	}
}

// add shadow only when templates are activated
.open .btn-app {
	box-shadow:4px 4px 2px 1px rgba(#000, 0.2);
}

// The most-popular apps in a circular thingo
.menu-round {
	position: absolute;
	bottom:0;
	right:0;
	z-index:3;
	
	.btn-app {
		bottom:0.25em;
		right:0.25em;
		transition:0.4s;
	}
	
	// position of templates when activated
	&.open {
		.btn-app:nth-of-type(1){
			right:0.5em;
			bottom:4.25em;
			transition-delay:0.2s;
		}
		.btn-app:nth-of-type(2){
			right:3.5em;
			bottom:3.5em;
			transition-delay:0.1s;
		}
		.btn-app:nth-of-type(3){
			right:4.25em;
			bottom:0.5em;
		}
	}	

}

// stacked template icons
.menu-line {
	position: absolute;
	z-index:2;
	
	.btn-app {
		bottom:0;
		right:0.5em;
		transition:0.3s;
		transition-delay:0.5s;
	}
	
	&.open {
		// first one. add 3 to each subsequent template
		$bottom:4.25em;
		$templates:7;
		
		.btn-app:nth-of-type(1) {
			bottom:$bottom;
		}
		
		// align each template item on top of the next
		@for $i from 1 through $templates {
			.btn-app:nth-of-type(#{$i}) {
				bottom:$bottom + 3 * $i;
			}
		}
	}	
	
}

</style>