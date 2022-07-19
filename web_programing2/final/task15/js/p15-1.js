let rate = document.getElementById("rate");
let yen = document.getElementById("yen");
let doll = document.getElementById("doll");
yen.addEventListener("input", function(){
  doll.value = yen.value / rate.value;
});
doll.addEventListener("input", function(){
  yen.value = doll.value * rate.value;
});
