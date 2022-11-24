<template>
  <div class="container">
    <div class="menu-toggle" @click="clickMenu" :class="{ open: isClicked }">
      <span class="fa fa-plus menu-bttn"></span>
    </div>
    
    <div class="menu-round" :class="{ open: isClicked }">
      <div class="btn-app" @click="goTo('time')">
        <div class="fa fa-solid fa-clock"></div>
				<div class="btn-text btn-text-github"><span>Time</span></div>
      </div>
      <div class="btn-app" @click="goTo('home')">
        <div class="fa fa-solid fa-house"></div>
				<div class="btn-text btn-text-home"><span>Home</span></div>
      </div>
      <div class="btn-app" @click="search">
        <div class="fa fa-solid fa-magnifying-glass"></div>
				<div class="btn-text btn-text-search"><span>Search</span></div>
      </div>
    </div>
    
    <div class="menu-line" :class="{ open: isClicked }">
      <div class="btn-app"  @click="openGithub">
        <div class="fa fa-brands fa-github"></div>
				<div class="btn-text"><span>Github</span></div>
      </div>
      <div class="btn-app">
        <div class="fa fa-solid fa-face-smile-wink"></div>
				<!-- <i class="fa-solid fa-face-smile-tongue"></i> -->
				<div class="btn-text"><span>Celebrity</span></div>
      </div>
      <!-- <div class="btn-app">
        <div class="fa fa-video-camera"></div> 
				<div class="btn-text"><span>Profile</span></div>
      </div>
      <div class="btn-app " @click="$store.dispatch('getUserProfile')">
        <div class="fa fa-solid fa-clock"></div>
				<div class="btn-text"><span>Profile</span></div>
      </div> -->
      <div class="btn-app signup-btn" @click="popUp('signup')">
        <div class="fa fa-solid fa-user-plus"></div>
				<div class="btn-text"><span>Signup</span></div>
      </div>
      <div class="btn-app login-btn" @click="popUp('login')" v-if="token == null">
        <!-- <div class="fa fa-solid fa-right-to-bracket" style="--fa-primary-color: gold;"></div> -->
        <div><i class="fa fa-solid fa-right-to-bracket"></i></div>
				<div class="btn-text"><span>Login</span></div>
      </div>
      <div class="btn-app logout-btn"  @click="logOut" v-if="token">
        <!-- <div class="fa fa-solid fa-right-to-bracket" style="--fa-primary-color: gold;"></div> -->
        <div><i class="fa fa-solid fa-right-from-bracket"></i></div>
				<div class="btn-text"><span>Logout</span></div>
      </div>
      <div class="btn-app	 profile-btn"  @click="goTo('profile')" @mouseover="profileSub">
        <!-- <div class="fa fa-vine"></div> -->
        <div><i class="fa fa-solid fa-user"></i></div>
				<div class="btn-text"><span>Profile</span></div>
      </div>
    </div>
    
    
  </div>
</template>

<script>
import 'animate.css';

export default {
  name: 'MenuBar2',
	computed: {
		token() {
			return this.$store.state.token
		}
	},
  data() {
    return {
      isClicked: false,
    }
  },
  methods: {
    clickMenu() {
      this.isClicked = !this.isClicked
    },
    popUp(page) {
			this.$store.commit('POP_UP', page)
    },
    goTo(routeName) {
      this.$router.push({ name: routeName })
      this.isClicked = !this.isClicked
    },
		openGithub() {
			window.open('https://github.com/oth54477/TimeCinema')
		},
		search(event) {
			const tag = event.target
			tag.class = 
			console.log(tag)
		},
		logOut() {
			this.$store.commit('LOG_OUT')
		},
		profileSub() {

		}

  },
}
</script>

<style scoped lang="scss">
// style attribute {
//     --button-hover-background: var(--example-color-alt);
//     --button-color: var(--white);
//     --button-background: var(--example-color-alt);
//     --button-margin-bottom: 0;
// }
// .fa-right-to-bracket {
// 	--fa-inverse:$red

// }

.fa-right-to-bracket:before {
    content: "\f2f6";
}

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
// $green:#1ef0a0;
// $green:#232a28;
$green:#634141;
// $blue:#4644fd;
// $blue:rgb(133, 131, 131);
$blue:#996633;
$red:#ff3c4b;
$brown: #996633;
$mycolor: #663333;

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
	z-index: 999;
}

// this toggles the whole damn thing
.menu-toggle {
	@include circle(60px);
	background-color: $green;
	box-shadow:4px 4px 2px 1px rgba(#000, 0.2);
	
	position: absolute;
	z-index:999;
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
	
	// .fa-right-to-bracket {
	// 	color:#fff;
	// 	font-size:2em;
	// 	display:table-cell;
	// 	vertical-align:middle;
	// 	transition:0.4s;
	// }

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
	
	display: flex;
	justify-content: center;
	align-items: center;

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

.btn-app {
	transition: transform .2s;
}
.btn-app:hover {
	transition: transform .2s;
  transform: scale(1.25); /* (150% zoom - Note: if the zoom is too large, it will go outside of the viewport) */
}

.btn-app:hover > div > i {
	color: #634141;
}

.btn-app:hover > div:nth-child(1) {
	color: #634141;
}

.btn-app:hover > .btn-text {
	opacity: 1;
}

.menu-toggle {

}

.menu-toggle {
	transition: transform .2s;
}
.menu-toggle:hover {
	transition: transform .2s;
  transform: scale(1.25); /* (150% zoom - Note: if the zoom is too large, it will go outside of the viewport) */
}
// .menu-toggle:hover > span {
// 	color: #ffeb00;
// }

.btn-text{
	position: absolute;
	top: 0.8vh;
	left: -3.7vw;
	color: black;
	font-weight: 600;
	border-radius: 10px;
	width: 4vw;
	height: 2.5vh;
	display: flex;
	font-size: 18px;
	align-items: center;
	justify-content: center;
	opacity: 0;
}

.btn-text-home {
	transform: translate3d(0.7vw, -3vh, 0px) rotate(35deg);
}
.btn-text-github {
	transform: translate3d(0.5vw, -3.5vh, 0px) rotate(35deg);
}
.btn-text-search {
	transform: translate3d(0.7vw, -2.7vh, 0px) rotate(35deg);
}

// 다크그린 다크 네이비 -> 진한색
</style>