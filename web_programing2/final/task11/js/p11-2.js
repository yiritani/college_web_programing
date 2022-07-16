let querySelector = document.querySelectorAll('#liEventListener')
for (let i = 0; i < querySelector.length; i++) {
  querySelector[i].addEventListener('click', (e) => {
    e.target.classList.toggle('transform1')
    e.target.classList.toggle('animation1')
  })
}

document.querySelectorAll('#ulEventListener').forEach((ul) => {
  ul.addEventListener('click', (e) => {
    e.target.classList.toggle('transform1')
    e.target.classList.toggle('animation1')
  })
})
