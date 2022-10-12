<template>
    <div class="loader">
	<div class="wrapper">
		<span class="line-1"></span>
		<span class="line-2"></span>
		<span class="line-3"></span>
		<span class="line-4"></span>
		<span class="line-5"></span>
		<span class="line-6"></span>
		<span class="line-7"></span>
		<span class="line-8"></span>
		<span class="line-9"></span>
		<span class="line-10"></span>
		<span class="line-11"></span>
		<span class="line-12"></span>
		<span class="line-13"></span>
		<span class="line-14"></span>
		<span class="line-15"></span>
		<span class="line-16"></span>
		<span class="line-17"></span>
		<span class="line-18"></span>
		<span class="line-19"></span>
		<span class="line-20"></span>
		<span class="line-21"></span>
		<span class="line-22"></span>
		<span class="line-23"></span>
		<span class="line-24"></span>
		<span class="line-25"></span>
		<span class="line-26"></span>
		<span class="line-27"></span>
		<span class="line-28"></span>
		<span class="line-29"></span>
		<span class="line-30"></span>
<!--		<span class="line-31"></span>
		<span class="line-32"></span>
		<span class="line-33"></span>
		<span class="line-34"></span>
		<span class="line-35"></span>
		<span class="line-36"></span>
		<span class="line-37"></span>
		<span class="line-38"></span>
		<span class="line-39"></span>
<span class="line-40"></span>
		<span class="line-41"></span>
		<span class="line-42"></span>
		<span class="line-43"></span>
		<span class="line-44"></span>
		<span class="line-45"></span>
		<span class="line-46"></span>
		<span class="line-47"></span>
		<span class="line-48"></span>
		<span class="line-49"></span>
		<span class="line-50"></span>-->
	</div>
  
  <!-- Spaceship by [Aleks](https://codepen.io/achudars/)'s Pen [Spaceship](https://codepen.io/achudars/pen/sbDdm/) -->
 <div id='center'>
  <div id='spaceship'>
    <div id='window'></div>
  </div>
  <div id='tail'></div>
   <div class="tail-2"></div>
  <div id='left-wing'></div>
  <div id='right-wing'></div>
  <div id='exhaust'></div>
  <div id='tail'></div>
</div>
  
</div>

</template>
<style scoped>
body {
  background-color: #444349;
}

.loader {
  background-color: #444349;
  width: 100%;
  height: 100vh;
  overflow: hidden;
  position: fixed;
  left: 50%;
  -moz-transform: translateX(-50%);
  -ms-transform: translateX(-50%);
  -webkit-transform: translateX(-50%);
  transform: translateX(-50%);
  z-index: 9999;
}
.loader span {
  position: relative;
  display: block;
  width: 400px;
  height: 2px;
}

.wrapper {
  width: 100%;
  height: 100%;
}

.line-1 {
  left: 27vw;
  background: rgba(255, 255, 255, 0.13193);
  -moz-transform: rotate(-45deg) translate(0, 0.32);
  -ms-transform: rotate(-45deg) translate(0, 0.32);
  -webkit-transform: rotate(-45deg) translate(0, 0.32);
  transform: rotate(-45deg) translate(0, 0.32);
  -moz-animation: line-1 4s linear infinite;
  -webkit-animation: line-1 4s linear infinite;
  animation: line-1 4s linear infinite;
}

.line-2 {
  left: 12vw;
  background: rgba(255, 255, 255, 0.10968);
  -moz-transform: rotate(-45deg) translate(0, 0.22836);
  -ms-transform: rotate(-45deg) translate(0, 0.22836);
  -webkit-transform: rotate(-45deg) translate(0, 0.22836);
  transform: rotate(-45deg) translate(0, 0.22836);
  -moz-animation: line-2 2s linear infinite;
  -webkit-animation: line-2 2s linear infinite;
  animation: line-2 2s linear infinite;
}

.line-3 {
  left: 37vw;
  background: rgba(255, 255, 255, 0.22501);
  -moz-transform: rotate(-45deg) translate(0, 1.84667);
  -ms-transform: rotate(-45deg) translate(0, 1.84667);
  -webkit-transform: rotate(-45deg) translate(0, 1.84667);
  transform: rotate(-45deg) translate(0, 1.84667);
  -moz-animation: line-3 2s linear infinite;
  -webkit-animation: line-3 2s linear infinite;
  animation: line-3 2s linear infinite;
}

.line-4 {
  left: 61vw;
  background: rgba(255, 255, 255, 0.22761);
  -moz-transform: rotate(-45deg) translate(0, 0.61892);
  -ms-transform: rotate(-45deg) translate(0, 0.61892);
  -webkit-transform: rotate(-45deg) translate(0, 0.61892);
  transform: rotate(-45deg) translate(0, 0.61892);
  -moz-animation: line-4 4s linear infinite;
  -webkit-animation: line-4 4s linear infinite;
  animation: line-4 4s linear infinite;
}

.line-5 {
  left: 62vw;
  background: rgba(255, 255, 255, 0.19616);
  -moz-transform: rotate(-45deg) translate(0, 0.01429);
  -ms-transform: rotate(-45deg) translate(0, 0.01429);
  -webkit-transform: rotate(-45deg) translate(0, 0.01429);
  transform: rotate(-45deg) translate(0, 0.01429);
  -moz-animation: line-5 2s linear infinite;
  -webkit-animation: line-5 2s linear infinite;
  animation: line-5 2s linear infinite;
}

.line-6 {
  left: 45vw;
  background: rgba(255, 255, 255, 0.11971);
  -moz-transform: rotate(-45deg) translate(0, 2.08571);
  -ms-transform: rotate(-45deg) translate(0, 2.08571);
  -webkit-transform: rotate(-45deg) translate(0, 2.08571);
  transform: rotate(-45deg) translate(0, 2.08571);
  -moz-animation: line-6 2s linear infinite;
  -webkit-animation: line-6 2s linear infinite;
  animation: line-6 2s linear infinite;
}

.line-7 {
  left: 88vw;
  background: rgba(255, 255, 255, 0.22519);
  -moz-transform: rotate(-45deg) translate(0, 0.22642);
  -ms-transform: rotate(-45deg) translate(0, 0.22642);
  -webkit-transform: rotate(-45deg) translate(0, 0.22642);
  transform: rotate(-45deg) translate(0, 0.22642);
  -moz-animation: line-7 2s linear infinite;
  -webkit-animation: line-7 2s linear infinite;
  animation: line-7 2s linear infinite;
}

.line-8 {
  left: 95vw;
  background: rgba(255, 255, 255, 0.17896);
  -moz-transform: rotate(-45deg) translate(0, 0.33939);
  -ms-transform: rotate(-45deg) translate(0, 0.33939);
  -webkit-transform: rotate(-45deg) translate(0, 0.33939);
  transform: rotate(-45deg) translate(0, 0.33939);
  -moz-animation: line-8 2s linear infinite;
  -webkit-animation: line-8 2s linear infinite;
  animation: line-8 2s linear infinite;
}

.line-9 {
  left: 71vw;
  background: rgba(255, 255, 255, 0.2433);
  -moz-transform: rotate(-45deg) translate(0, 0.0642);
  -ms-transform: rotate(-45deg) translate(0, 0.0642);
  -webkit-transform: rotate(-45deg) translate(0, 0.0642);
  transform: rotate(-45deg) translate(0, 0.0642);
  -moz-animation: line-9 3s linear infinite;
  -webkit-animation: line-9 3s linear infinite;
  animation: line-9 3s linear infinite;
}

.line-10 {
  left: 97vw;
  background: rgba(255, 255, 255, 0.21736);
  -moz-transform: rotate(-45deg) translate(0, 0.56757);
  -ms-transform: rotate(-45deg) translate(0, 0.56757);
  -webkit-transform: rotate(-45deg) translate(0, 0.56757);
  transform: rotate(-45deg) translate(0, 0.56757);
  -moz-animation: line-10 4s linear infinite;
  -webkit-animation: line-10 4s linear infinite;
  animation: line-10 4s linear infinite;
}

@-moz-keyframes line-1 {
  0% {
    -moz-transform: rotate(-45deg) translate(400px, 78.43137px);
    transform: rotate(-45deg) translate(400px, 78.43137px);
  }
  100% {
    -moz-transform: rotate(-45deg) translate(-376%, 78.43137px);
    transform: rotate(-45deg) translate(-376%, 78.43137px);
  }
}
@-webkit-keyframes line-1 {
  0% {
    -webkit-transform: rotate(-45deg) translate(400px, 78.43137px);
    transform: rotate(-45deg) translate(400px, 78.43137px);
  }
  100% {
    -webkit-transform: rotate(-45deg) translate(-453%, 78.43137px);
    transform: rotate(-45deg) translate(-453%, 78.43137px);
  }
}
@keyframes line-1 {
  0% {
    -moz-transform: rotate(-45deg) translate(400px, 78.43137px);
    -ms-transform: rotate(-45deg) translate(400px, 78.43137px);
    -webkit-transform: rotate(-45deg) translate(400px, 78.43137px);
    transform: rotate(-45deg) translate(400px, 78.43137px);
  }
  100% {
    -moz-transform: rotate(-45deg) translate(-414%, 78.43137px);
    -ms-transform: rotate(-45deg) translate(-414%, 78.43137px);
    -webkit-transform: rotate(-45deg) translate(-414%, 78.43137px);
    transform: rotate(-45deg) translate(-414%, 78.43137px);
  }
}
@-moz-keyframes line-2 {
  0% {
    -moz-transform: rotate(-45deg) translate(400px, 307.69231px);
    transform: rotate(-45deg) translate(400px, 307.69231px);
  }
  100% {
    -moz-transform: rotate(-45deg) translate(-430%, 307.69231px);
    transform: rotate(-45deg) translate(-430%, 307.69231px);
  }
}
@-webkit-keyframes line-2 {
  0% {
    -webkit-transform: rotate(-45deg) translate(400px, 307.69231px);
    transform: rotate(-45deg) translate(400px, 307.69231px);
  }
  100% {
    -webkit-transform: rotate(-45deg) translate(-426%, 307.69231px);
    transform: rotate(-45deg) translate(-426%, 307.69231px);
  }
}
@keyframes line-2 {
  0% {
    -moz-transform: rotate(-45deg) translate(400px, 307.69231px);
    -ms-transform: rotate(-45deg) translate(400px, 307.69231px);
    -webkit-transform: rotate(-45deg) translate(400px, 307.69231px);
    transform: rotate(-45deg) translate(400px, 307.69231px);
  }
  100% {
    -moz-transform: rotate(-45deg) translate(-324%, 307.69231px);
    -ms-transform: rotate(-45deg) translate(-324%, 307.69231px);
    -webkit-transform: rotate(-45deg) translate(-324%, 307.69231px);
    transform: rotate(-45deg) translate(-324%, 307.69231px);
  }
}
@-moz-keyframes line-3 {
  0% {
    -moz-transform: rotate(-45deg) translate(400px, 72.72727px);
    transform: rotate(-45deg) translate(400px, 72.72727px);
  }
  100% {
    -moz-transform: rotate(-45deg) translate(-345%, 72.72727px);
    transform: rotate(-45deg) translate(-345%, 72.72727px);
  }
}
@-webkit-keyframes line-3 {
  0% {
    -webkit-transform: rotate(-45deg) translate(400px, 72.72727px);
    transform: rotate(-45deg) translate(400px, 72.72727px);
  }
  100% {
    -webkit-transform: rotate(-45deg) translate(-389%, 72.72727px);
    transform: rotate(-45deg) translate(-389%, 72.72727px);
  }
}
@keyframes line-3 {
  0% {
    -moz-transform: rotate(-45deg) translate(400px, 72.72727px);
    -ms-transform: rotate(-45deg) translate(400px, 72.72727px);
    -webkit-transform: rotate(-45deg) translate(400px, 72.72727px);
    transform: rotate(-45deg) translate(400px, 72.72727px);
  }
  100% {
    -moz-transform: rotate(-45deg) translate(-492%, 72.72727px);
    -ms-transform: rotate(-45deg) translate(-492%, 72.72727px);
    -webkit-transform: rotate(-45deg) translate(-492%, 72.72727px);
    transform: rotate(-45deg) translate(-492%, 72.72727px);
  }
}
@-moz-keyframes line-4 {
  0% {
    -moz-transform: rotate(-45deg) translate(400px, 76.92308px);
    transform: rotate(-45deg) translate(400px, 76.92308px);
  }
  100% {
    -moz-transform: rotate(-45deg) translate(-465%, 76.92308px);
    transform: rotate(-45deg) translate(-465%, 76.92308px);
  }
}
@-webkit-keyframes line-4 {
  0% {
    -webkit-transform: rotate(-45deg) translate(400px, 76.92308px);
    transform: rotate(-45deg) translate(400px, 76.92308px);
  }
  100% {
    -webkit-transform: rotate(-45deg) translate(-384%, 76.92308px);
    transform: rotate(-45deg) translate(-384%, 76.92308px);
  }
}
@keyframes line-4 {
  0% {
    -moz-transform: rotate(-45deg) translate(400px, 76.92308px);
    -ms-transform: rotate(-45deg) translate(400px, 76.92308px);
    -webkit-transform: rotate(-45deg) translate(400px, 76.92308px);
    transform: rotate(-45deg) translate(400px, 76.92308px);
  }
  100% {
    -moz-transform: rotate(-45deg) translate(-485%, 76.92308px);
    -ms-transform: rotate(-45deg) translate(-485%, 76.92308px);
    -webkit-transform: rotate(-45deg) translate(-485%, 76.92308px);
    transform: rotate(-45deg) translate(-485%, 76.92308px);
  }
}
@-moz-keyframes line-5 {
  0% {
    -moz-transform: rotate(-45deg) translate(400px, 85.10638px);
    transform: rotate(-45deg) translate(400px, 85.10638px);
  }
  100% {
    -moz-transform: rotate(-45deg) translate(-463%, 85.10638px);
    transform: rotate(-45deg) translate(-463%, 85.10638px);
  }
}
@-webkit-keyframes line-5 {
  0% {
    -webkit-transform: rotate(-45deg) translate(400px, 85.10638px);
    transform: rotate(-45deg) translate(400px, 85.10638px);
  }
  100% {
    -webkit-transform: rotate(-45deg) translate(-329%, 85.10638px);
    transform: rotate(-45deg) translate(-329%, 85.10638px);
  }
}
@keyframes line-5 {
  0% {
    -moz-transform: rotate(-45deg) translate(400px, 85.10638px);
    -ms-transform: rotate(-45deg) translate(400px, 85.10638px);
    -webkit-transform: rotate(-45deg) translate(400px, 85.10638px);
    transform: rotate(-45deg) translate(400px, 85.10638px);
  }
  100% {
    -moz-transform: rotate(-45deg) translate(-304%, 85.10638px);
    -ms-transform: rotate(-45deg) translate(-304%, 85.10638px);
    -webkit-transform: rotate(-45deg) translate(-304%, 85.10638px);
    transform: rotate(-45deg) translate(-304%, 85.10638px);
  }
}
@-moz-keyframes line-6 {
  0% {
    -moz-transform: rotate(-45deg) translate(400px, 1000px);
    transform: rotate(-45deg) translate(400px, 1000px);
  }
  100% {
    -moz-transform: rotate(-45deg) translate(-345%, 1000px);
    transform: rotate(-45deg) translate(-345%, 1000px);
  }
}
@-webkit-keyframes line-6 {
  0% {
    -webkit-transform: rotate(-45deg) translate(400px, 1000px);
    transform: rotate(-45deg) translate(400px, 1000px);
  }
  100% {
    -webkit-transform: rotate(-45deg) translate(-482%, 1000px);
    transform: rotate(-45deg) translate(-482%, 1000px);
  }
}
@keyframes line-6 {
  0% {
    -moz-transform: rotate(-45deg) translate(400px, 1000px);
    -ms-transform: rotate(-45deg) translate(400px, 1000px);
    -webkit-transform: rotate(-45deg) translate(400px, 1000px);
    transform: rotate(-45deg) translate(400px, 1000px);
  }
  100% {
    -moz-transform: rotate(-45deg) translate(-302%, 1000px);
    -ms-transform: rotate(-45deg) translate(-302%, 1000px);
    -webkit-transform: rotate(-45deg) translate(-302%, 1000px);
    transform: rotate(-45deg) translate(-302%, 1000px);
  }
}
@-moz-keyframes line-7 {
  0% {
    -moz-transform: rotate(-45deg) translate(400px, 58.82353px);
    transform: rotate(-45deg) translate(400px, 58.82353px);
  }
  100% {
    -moz-transform: rotate(-45deg) translate(-349%, 58.82353px);
    transform: rotate(-45deg) translate(-349%, 58.82353px);
  }
}
@-webkit-keyframes line-7 {
  0% {
    -webkit-transform: rotate(-45deg) translate(400px, 58.82353px);
    transform: rotate(-45deg) translate(400px, 58.82353px);
  }
  100% {
    -webkit-transform: rotate(-45deg) translate(-481%, 58.82353px);
    transform: rotate(-45deg) translate(-481%, 58.82353px);
  }
}
@keyframes line-7 {
  0% {
    -moz-transform: rotate(-45deg) translate(400px, 58.82353px);
    -ms-transform: rotate(-45deg) translate(400px, 58.82353px);
    -webkit-transform: rotate(-45deg) translate(400px, 58.82353px);
    transform: rotate(-45deg) translate(400px, 58.82353px);
  }
  100% {
    -moz-transform: rotate(-45deg) translate(-371%, 58.82353px);
    -ms-transform: rotate(-45deg) translate(-371%, 58.82353px);
    -webkit-transform: rotate(-45deg) translate(-371%, 58.82353px);
    transform: rotate(-45deg) translate(-371%, 58.82353px);
  }
}
@-moz-keyframes line-8 {
  0% {
    -moz-transform: rotate(-45deg) translate(400px, 133.33333px);
    transform: rotate(-45deg) translate(400px, 133.33333px);
  }
  100% {
    -moz-transform: rotate(-45deg) translate(-421%, 133.33333px);
    transform: rotate(-45deg) translate(-421%, 133.33333px);
  }
}
@-webkit-keyframes line-8 {
  0% {
    -webkit-transform: rotate(-45deg) translate(400px, 133.33333px);
    transform: rotate(-45deg) translate(400px, 133.33333px);
  }
  100% {
    -webkit-transform: rotate(-45deg) translate(-440%, 133.33333px);
    transform: rotate(-45deg) translate(-440%, 133.33333px);
  }
}
@keyframes line-8 {
  0% {
    -moz-transform: rotate(-45deg) translate(400px, 133.33333px);
    -ms-transform: rotate(-45deg) translate(400px, 133.33333px);
    -webkit-transform: rotate(-45deg) translate(400px, 133.33333px);
    transform: rotate(-45deg) translate(400px, 133.33333px);
  }
  100% {
    -moz-transform: rotate(-45deg) translate(-351%, 133.33333px);
    -ms-transform: rotate(-45deg) translate(-351%, 133.33333px);
    -webkit-transform: rotate(-45deg) translate(-351%, 133.33333px);
    transform: rotate(-45deg) translate(-351%, 133.33333px);
  }
}
@-moz-keyframes line-9 {
  0% {
    -moz-transform: rotate(-45deg) translate(400px, 50.63291px);
    transform: rotate(-45deg) translate(400px, 50.63291px);
  }
  100% {
    -moz-transform: rotate(-45deg) translate(-386%, 50.63291px);
    transform: rotate(-45deg) translate(-386%, 50.63291px);
  }
}
@-webkit-keyframes line-9 {
  0% {
    -webkit-transform: rotate(-45deg) translate(400px, 50.63291px);
    transform: rotate(-45deg) translate(400px, 50.63291px);
  }
  100% {
    -webkit-transform: rotate(-45deg) translate(-341%, 50.63291px);
    transform: rotate(-45deg) translate(-341%, 50.63291px);
  }
}
@keyframes line-9 {
  0% {
    -moz-transform: rotate(-45deg) translate(400px, 50.63291px);
    -ms-transform: rotate(-45deg) translate(400px, 50.63291px);
    -webkit-transform: rotate(-45deg) translate(400px, 50.63291px);
    transform: rotate(-45deg) translate(400px, 50.63291px);
  }
  100% {
    -moz-transform: rotate(-45deg) translate(-332%, 50.63291px);
    -ms-transform: rotate(-45deg) translate(-332%, 50.63291px);
    -webkit-transform: rotate(-45deg) translate(-332%, 50.63291px);
    transform: rotate(-45deg) translate(-332%, 50.63291px);
  }
}
@-moz-keyframes line-10 {
  0% {
    -moz-transform: rotate(-45deg) translate(400px, 44.44444px);
    transform: rotate(-45deg) translate(400px, 44.44444px);
  }
  100% {
    -moz-transform: rotate(-45deg) translate(-469%, 44.44444px);
    transform: rotate(-45deg) translate(-469%, 44.44444px);
  }
}
@-webkit-keyframes line-10 {
  0% {
    -webkit-transform: rotate(-45deg) translate(400px, 44.44444px);
    transform: rotate(-45deg) translate(400px, 44.44444px);
  }
  100% {
    -webkit-transform: rotate(-45deg) translate(-436%, 44.44444px);
    transform: rotate(-45deg) translate(-436%, 44.44444px);
  }
}
@keyframes line-10 {
  0% {
    -moz-transform: rotate(-45deg) translate(400px, 44.44444px);
    -ms-transform: rotate(-45deg) translate(400px, 44.44444px);
    -webkit-transform: rotate(-45deg) translate(400px, 44.44444px);
    transform: rotate(-45deg) translate(400px, 44.44444px);
  }
  100% {
    -moz-transform: rotate(-45deg) translate(-438%, 44.44444px);
    -ms-transform: rotate(-45deg) translate(-438%, 44.44444px);
    -webkit-transform: rotate(-45deg) translate(-438%, 44.44444px);
    transform: rotate(-45deg) translate(-438%, 44.44444px);
  }
}
#center {
  width: 100px;
  height: 100px;
  position: absolute;
  left: 50vw;
  top: 50vh;
  transform: rotate(45deg);
  animation: fly 6s infinite linear;
}

#spaceship {
  position: inherit;
  left: 50%;
  margin-left: -45px;
  height: 90px;
  width: 65px;
  background: #fff;
  border-radius: 100px 100px 20px 20px;
  z-index: 3;
}

#window {
  position: inherit;
  margin-top: 35px;
  margin-left: 35px;
  height: 20px;
  width: 20px;
  background: #cecece;
  border-radius: 50%;
  border: 10px solid #562449;
  animation: window 4s infinite linear;
}

#tail {
  top: 50%;
  left: 50%;
  margin-left: -41px;
  margin-top: 40px;
  position: inherit;
  height: 0;
  width: 60px;
  border-bottom: 30px solid #cecece;
  border-left: 20px solid transparent;
  border-right: 20px solid transparent;
  padding: 0 2px 0 0;
}

#left-wing {
  top: 50%;
  left: 50%;
  margin-left: 24px;
  margin-top: -5px;
  position: inherit;
  height: 0;
  width: 10px;
  border-bottom: 60px solid #cecece;
  border-left: 0px solid transparent;
  border-right: 30px solid transparent;
  padding: 0 2px 0 0;
  animation: from-to 4s infinite linear;
}

#right-wing {
  top: 50%;
  left: 50%;
  margin-left: -75px;
  margin-top: -5px;
  position: inherit;
  height: 0;
  width: 10px;
  border-bottom: 60px solid #cecece;
  border-left: 30px solid transparent;
  border-right: 0px solid transparent;
  padding: 0 2px 0 0;
  animation: to-from 4s infinite linear;
}

#exhaust {
  left: 50%;
  top: 50%;
  margin-left: -33px;
  margin-top: 20px;
  position: inherit;
  background: #f2b31b;
  width: 40px;
  height: 40px;
  border-radius: 50px 10px 50px 50px;
  transform: rotate(135deg);
}

#tail {
  left: 50%;
  top: 50%;
  margin-left: -31px;
  margin-top: 40px;
  position: inherit;
  width: 0px;
  height: 0px;
  border-style: solid;
  border-width: 100px 17px 0 17px;
  border-color: #f2b31b transparent transparent transparent;
  animation: burn .1s infinite linear;
  z-index: 1;
}

.tail-2 {
  left: 50%;
  top: 50%;
  margin-left: -31px;
  margin-top: 40px;
  position: inherit;
  width: 0px;
  height: 0px;
  border-style: solid;
  border-width: 100px 17px 0 17px;
  border-color: #ede67d transparent transparent transparent;
  animation: burn-2 .1s infinite linear;
  z-index: 2;
}

@keyframes burn {
  0% {
    border-width: 100px 17px 0 17px;
  }
  25% {
    border-width: 100px 17px 0 17px;
  }
  50% {
    border-width: 125px 17px 0 17px;
  }
  75% {
    border-width: 75px 17px 0 17px;
  }
  100% {
    border-width: 100px 17px 0 17px;
  }
}
@keyframes burn-2 {
  0% {
    border-width: 50px 17px 0 17px;
  }
  25% {
    border-width: 50px 17px 0 17px;
  }
  50% {
    border-width: 63px 17px 0 17px;
  }
  75% {
    border-width: 38px 17px 0 17px;
  }
  100% {
    border-width: 50px 17px 0 17px;
  }
}
@keyframes from-to {
  0% {
    margin-left: 19px;
    width: 10px;
    border-bottom: 30px solid #cecece;
    border-left: 0px solid transparent;
    border-right: 15px solid transparent;
  }
  50% {
    margin-left: 15px;
    width: 5px;
    border-bottom: 30px solid #cecece;
    border-left: 0px solid transparent;
    border-right: 8px solid transparent;
  }
  100% {
    margin-left: 19px;
    width: 10px;
    border-bottom: 30px solid #cecece;
    border-left: 0px solid transparent;
    border-right: 15px solid transparent;
  }
}
@keyframes to-from {
  0% {
    margin-left: -63px;
    width: 15px;
    border-bottom: 30px solid #cecece;
    border-left: 8px solid transparent;
    border-right: 0px solid transparent;
  }
  50% {
    margin-left: -70px;
    width: 15px;
    border-bottom: 30px solid #cecece;
    border-left: 16px solid transparent;
    border-right: 0px solid transparent;
  }
  100% {
    margin-left: -63px;
    width: 15px;
    border-bottom: 30px solid #cecece;
    border-left: 8px solid transparent;
    border-right: 0px solid transparent;
  }
}
@keyframes window {
  0% {
    margin-left: 13px;
  }
  50% {
    margin-left: 20px;
  }
  100% {
    margin-left: 13px;
  }
}
@keyframes fly {
  0% {
    left: 50%;
    top: 50%;
  }
  20%,35% {
    left: 40%;
    top: 40%;
  }
  50% {
    left: 50%;
    top: 45%;
  }
  57%,64% {
    left: 53%;
    top: 52%;
  }
  75%,85% {
    left: 58%;
    top: 65%;
  }
  100% {
    left: 50%;
    top: 50%;
  }
}
</style>
