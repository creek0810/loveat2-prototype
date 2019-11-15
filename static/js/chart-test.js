let tableItem = true;
let tableGender = true;

function toggleItem() {
  if(tableItem) {
    document.getElementById('item-analysis-table').classList.add("hidden");
    document.getElementById('item-analysis-chart').classList.remove("hidden");
  } else {
    document.getElementById('item-analysis-table').classList.remove("hidden");
    document.getElementById('item-analysis-chart').classList.add("hidden");
  }
  tableItem = !tableItem;
}

function toggleGender() {
  if(tableGender) {
    document.getElementById('gender-analysis-table').classList.add("hidden");
    document.getElementById('gender-analysis-chart').classList.remove("hidden");
  } else {
    document.getElementById('gender-analysis-table').classList.remove("hidden");
    document.getElementById('gender-analysis-chart').classList.add("hidden");
  }
  tableGender = !tableGender;
}


function drawItem() {
  const barChart = document.getElementById('item-bar-chart');
  const pieChart = document.getElementById('item-pie-chart');
  let myBarChart = new Chart(barChart, {
    type: 'bar',
    data: {
      labels: ["紅茶", "綠茶", "燻雞三明治", "乳酪三明治", "乳酪蛋餅", "豬肉漢堡", "不好喝的紅茶"],
      datasets: [{
        label: 'Groups',
        data: [100, 99, 97, 88, 80, 50, 0],
        backgroundColor: [
          "#60acfc", "#32d3eb", "#5bc49f", "#feb64d", "#ff7c7c",
          "#9287e7", "#27A1EA", "#4EBECD", "#9CDC82", "#FF9F69",
          "#E9668E", "#747BE1", "#39B3EA", "#40CEC7", "#D4EC59",
          "#FA816D", "#D660A8", "#6370DE", "#35C5EA", "#63D5B2",
          "#FFDA43", "#FB6E6C", "#B55CBD", "#668ED6", "#9FCDFD"
        ]
      }]
    }
  });
  let myPieChart = new Chart(pieChart, {
    type: 'pie',
    data: {
      labels: ["紅茶", "綠茶", "燻雞三明治", "乳酪三明治", "乳酪蛋餅", "豬肉漢堡", "不好喝的紅茶"],
      datasets: [{
        label: 'Groups',
        data: [100, 99, 97, 88, 80, 50, 0],
        backgroundColor: [
          "#60acfc", "#32d3eb", "#5bc49f", "#feb64d", "#ff7c7c",
          "#9287e7", "#27A1EA", "#4EBECD", "#9CDC82", "#FF9F69",
          "#E9668E", "#747BE1", "#39B3EA", "#40CEC7", "#D4EC59",
          "#FA816D", "#D660A8", "#6370DE", "#35C5EA", "#63D5B2",
          "#FFDA43", "#FB6E6C", "#B55CBD", "#668ED6", "#9FCDFD"
        ]
      }]
    }
  });
}

function drawGender() {
  const maleChart = document.getElementById('male-pie-chart');
  const femaleChart = document.getElementById('female-pie-chart');
  const genderChart = document.getElementById('gender-pie-chart');
  let myFemaleChart = new Chart(femaleChart, {
    type: 'pie',
    data: {
      labels: ["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60+"],
      datasets: [{
        label: 'Groups',
        data: [100, 156, 101 ,28, 789, 34, 200],
        backgroundColor: [
          "#60acfc", "#32d3eb", "#5bc49f", "#feb64d", "#ff7c7c",
          "#9287e7", "#27A1EA", "#4EBECD", "#9CDC82", "#FF9F69",
          "#E9668E", "#747BE1", "#39B3EA", "#40CEC7", "#D4EC59",
          "#FA816D", "#D660A8", "#6370DE", "#35C5EA", "#63D5B2",
          "#FFDA43", "#FB6E6C", "#B55CBD", "#668ED6", "#9FCDFD"
        ]
      }]
    }
  });
  let myMaleChart= new Chart(maleChart, {
    type: 'pie',
    data: {
      labels: ["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60+"],
      datasets: [{
        label: 'Groups',
        data: [1000, 1956, 501 ,98, 79, 394, 200],
        backgroundColor: [
          "#60acfc", "#32d3eb", "#5bc49f", "#feb64d", "#ff7c7c",
          "#9287e7", "#27A1EA", "#4EBECD", "#9CDC82", "#FF9F69",
          "#E9668E", "#747BE1", "#39B3EA", "#40CEC7", "#D4EC59",
          "#FA816D", "#D660A8", "#6370DE", "#35C5EA", "#63D5B2",
          "#FFDA43", "#FB6E6C", "#B55CBD", "#668ED6", "#9FCDFD"
        ]
      }]
    }
  });
  let myGenderChart = new Chart(genderChart, {
    type: 'pie',
    data: {
      labels: ["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60+"],
      datasets: [{
        label: 'Groups',
        data: [10, 1056, 81 ,18, 78, 384, 20],
        backgroundColor: [
          "#60acfc", "#32d3eb", "#5bc49f", "#feb64d", "#ff7c7c",
          "#9287e7", "#27A1EA", "#4EBECD", "#9CDC82", "#FF9F69",
          "#E9668E", "#747BE1", "#39B3EA", "#40CEC7", "#D4EC59",
          "#FA816D", "#D660A8", "#6370DE", "#35C5EA", "#63D5B2",
          "#FFDA43", "#FB6E6C", "#B55CBD", "#668ED6", "#9FCDFD"
        ]
      }]
    }
  });
}

function init() {
  document.getElementById('item-analysis-btn').addEventListener("click", toggleItem);
  document.getElementById('gender-analysis-btn').addEventListener("click", toggleGender);
  drawItem();
  drawGender();
}
window.addEventListener('load', init);