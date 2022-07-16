document.querySelector("#textbox").addEventListener("input", () => {
  document.querySelector("#textboxResult").innerHTML = document.querySelector("#textbox").value;
});
document.querySelector("#textarea").addEventListener("input", () => {
  document.querySelector("#textAreaResult").innerHTML = document.querySelector("#textarea").value;
});
document.querySelector("#slider").addEventListener("input", () => {
  document.querySelector("#sliderResult").innerHTML = document.querySelector("#slider").value;
});
let checkArr = [];
document.querySelectorAll("input[type='checkbox']").forEach((chk) => {
  chk.addEventListener('change', (e) => {
    console.log(e.target.checked);
    if (e.target.checked) {
      checkArr.push(e.target.value);
    } else {
      checkArr.splice(checkArr.indexOf(e.target.value), 1);
    }
    console.log(checkArr)
    document.querySelector("#checkboxresult").innerHTML = checkArr;
  });
});
document.querySelectorAll("input[type='radio']").forEach((chk) => {
  chk.addEventListener('change', (e) => {
    document.querySelector("#radioresult").innerHTML = e.target.value;
  });
});
document.querySelector("#selectBoxId").addEventListener('change', (e) => {
  document.querySelector("#selectboxresult").innerHTML = e.target.value;
});
let menuArr = [];
document.querySelector("#multiSelectId").addEventListener('change', (e) => {
  console.log(e.target.value)
  if (menuArr.filter(item => item === e.target.value).length === 0) {
    menuArr.push(e.target.value);
  } else {
    menuArr.splice(menuArr.indexOf(e.target.value), 1);
  }
  console.log(menuArr)
  document.querySelector("#multiSelectresult").innerHTML = menuArr;
});
