let c={x:0,y:0,r:100}
let timerID = null;
const cv = document.querySelector('canvas')
const gc = cv.getContext('2d')
const btn = document.querySelector('#btn')
btn.addEventListener('click',()=>{
  if (timerID==null) {
    timerID=setInterval(draw, 1);
  }else{
    clearInterval(timerID);
    timerID=null;
  }
})

function draw() {
  c.x += 1;
  c.y += 1;
  gc.clearRect(0,0,cv.width,cv.height);
  gc.beginPath();
  gc.fillStyle = 'red';
  gc.arc(c.x,c.y,c.r,0,Math.PI*2,true);
  gc.fill();
}
