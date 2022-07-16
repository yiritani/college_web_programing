let timerID = null;
const cv = document.querySelector('canvas')
const btn = document.querySelector('#btn')
const stopBtn = document.querySelector('#stopBtn')
const colorArray = ['red','blue','green','yellow','orange','pink']
const circleArray = []
const circleObjArray = []
btn.addEventListener('click',()=>{
  generateRandomCircle()
  if (timerID==null) {
    timerID=setInterval(moveCircles, 20);
  }
})
stopBtn.addEventListener('click',()=>{
  clearInterval(timerID);
  timerID=null;
})

function generateRandomNum(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
function chooseRandomcolor() {
  return colorArray[Math.floor(Math.random() * colorArray.length)];
}

function generateRandomCircle() {
  let c={x:0,y:0,r:100}
  c.x = generateRandomNum(50, 550);
  c.y = generateRandomNum(50, 350);
  c.r = generateRandomNum(20, 50);
  let gc = cv.getContext('2d')
  gc.beginPath();
  gc.strokeStyle = chooseRandomcolor();
  gc.arc(c.x,c.y,c.r,0,Math.PI*2,true);
  gc.lineWidth = 2;
  gc.stroke();
  circleArray.push(c)
  circleObjArray.push(gc)
  console.log(circleArray)
}
function moveCircles() {
  console.log(circleArray[1])
  for (let i=0; i<circleArray.length; i++) {
    circleArray[i].x -= 1;
    circleArray[i].y -= 1;
    circleObjArray[i].clearRect(0,0,600,400);
    circleObjArray[i].beginPath();
    circleObjArray[i].arc(circleArray[i].x,circleArray[i].y,circleArray[i].r,0,Math.PI*2,true);
    circleObjArray[i].lineWidth = 2;
    circleObjArray[i].stroke();
  }
}
