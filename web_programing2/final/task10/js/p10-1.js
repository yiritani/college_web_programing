const textButton = document.querySelector('#textbutton');
const textAreaButton = document.querySelector('#textAreabutton');
const sliderButton = document.querySelector('#sliderbutton');
const selectboxButton = document.querySelector('#selectboxbutton');
textButton.addEventListener('click', () => {
  document.querySelector("#textboxResult").textContent = displayValue('#textbox');
});
textAreaButton.addEventListener('click', () => {
  document.querySelector("#textAreaResult").textContent = displayValue('#textarea');
});
sliderButton.addEventListener('click', () => {
  document.querySelector("#sliderResult").textContent = displayValue('#slider');
});
selectboxButton.addEventListener('click', () => {
  document.querySelector("#selectboxresult").textContent = displayValue('#selectBoxId');
});

function displayValue(inputId) {
  return document.querySelector(inputId).value;
}

const checkboxButton = document.querySelector("#checkboxbutton");
const radioButton = document.querySelector("#radiobutton");
checkboxButton.addEventListener('click', () => {
  document.querySelector("#checkboxresult").textContent = displayChoices('checkbox');
});
radioButton.addEventListener('click', () => {
  document.querySelector("#radioresult").textContent = displayChoices('radio');
});

function displayChoices(inputName) {
  const arr = [];
  const selected = document.getElementsByName(inputName);
  console.log(selected)
  for (let i = 0; i < selected.length; i++) {
    if (selected[i].checked) {
      arr.push(selected[i].value);
    }
  }
  return arr
}

const multiSelectButton = document.querySelector('#multiSelectbutton');
multiSelectButton.addEventListener('click', () => {
  document.querySelector("#multiSelectresult").textContent = multiSelect('multiSelectId');
});

function multiSelect(inputName) {
  const arr = [];
  const selected = document.getElementById(inputName).options;
  console.log(selected)
  for (let i = 0; i < selected.length; i++) {
    if (selected[i].selected) {
      arr.push(selected[i].value);
    }
  }
  return arr
}
