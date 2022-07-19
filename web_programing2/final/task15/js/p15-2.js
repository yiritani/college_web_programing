function addOrder(e) {
  const foodName = e.target.parentNode.parentNode.children[1].innerText;
  const li = document.createElement('li');
  li.innerText = foodName;
  document.getElementById('orderList').appendChild(li);
}

const chinjaoBtn = document.getElementById('chinjaoBtn');
chinjaoBtn.addEventListener('click', function(e) {
  addOrder(e)
});
const harumakiBtn = document.getElementById('harumakiBtn');
harumakiBtn.addEventListener('click', function(e) {
  addOrder(e)
});
const kushinsaiBtn = document.getElementById('kushinsaiBtn');
kushinsaiBtn.addEventListener('click', function(e) {
  addOrder(e)
});
const subutaBtn = document.getElementById('subutaBtn');
subutaBtn.addEventListener('click', function(e) {
  addOrder(e)
});
const tenshinBtn = document.getElementById('tenshinBtn');
tenshinBtn.addEventListener('click', function(e) {
  addOrder(e)
});
const serveButton = document.getElementById('serveButton');
serveButton.addEventListener('click', function(e) {
  const orderList = document.getElementById('orderList');
  const li = orderList.children[0];
  orderList.removeChild(li);
});
