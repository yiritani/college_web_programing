const kiyomizuBtn = document.querySelector('#kiyomizu');
const hushimiBtn = document.querySelector('#hushimi');
const kinkakuBtn = document.querySelector('#kinkaku');
const byoudouinBtn = document.querySelector('#byoudouin');

kiyomizuBtn.addEventListener("click", () => {
  const req = new XMLHttpRequest();
  req.addEventListener("load", () => {
    getData(req)
  });
  req.open("GET", "./media/kyoto-0.html");
  req.send()
  img.innerHTML = `<img src="${data.img}">`;
  text.innerHTML = `<p>${data.text}</p>`;
})
hushimiBtn.addEventListener("click", () => {
  const req = new XMLHttpRequest();
  req.addEventListener("load", () => {
    getData(req)
  });
  req.open("GET", "./media/kyoto-2.html");
  req.send()
  img.innerHTML = `<img src="${data.img}">`;
  text.innerHTML = `<p>${data.text}</p>`;
})
kinkakuBtn.addEventListener("click", () => {
  const req = new XMLHttpRequest();
  req.addEventListener("load", () => {
    getData(req)
  });
  req.open("GET", "./media/kyoto-1.html");
  req.send()
  img.innerHTML = `<img src="${data.img}">`;
  text.innerHTML = `<p>${data.text}</p>`;
})
byoudouinBtn.addEventListener("click", () => {
  const req = new XMLHttpRequest();
  req.addEventListener("load", () => {
    getData(req)
  });
  req.open("GET", "./media/kyoto-3.html");
  req.send()
  img.innerHTML = `<img src="${data.img}">`;
  text.innerHTML = `<p>${data.text}</p>`;
})

function getData(req) {
  document.querySelector("#content").innerHTML=req.responseText;
}
