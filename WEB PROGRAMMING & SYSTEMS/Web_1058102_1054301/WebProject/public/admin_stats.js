async function getData() {
  const response = await fetch("/morf_stats/1");
  const response1 = await fetch("/morf_stats/2");
  const data1 = await response1.json();
  const data = await response.json();
  console.log(data);
  console.log(data1);
  user_len = data.username_len;
  method = data.method_len;
  status_counter = data.status_counter;
  console.log(status_counter);
  status = data.status_len;

  console.log(method);
  console.log(status.split(","));

  console.log(data.web_object_a_a);
  console.log(data.aver_life);
  document.getElementById("users").innerHTML = data1;
  document.getElementById("url").innerHTML = data.url_len;
  document.getElementById("isp").innerHTML = 1;

  var array_method = [];
  var array_oc = [];
  for (let i = 0; i < method.length; i++) {
    for (let j = 0; j < method.length; j++) {
      array_method.push(method[i][0]);
      array_oc.push(method[i][1]);
    }
  }
  //console.log(array_method);
  //console.log(array_oc);
  const unique = (value, index, self) => {
    return self.indexOf(value) === index;
  };

  const uniqueMethods = array_method.filter(unique);
  const uniqueOc = array_oc.filter(unique);

  var ctx = document.getElementById("myChart");
  var myChart = new Chart(ctx, {
    type: "pie",
    data: {
      labels: uniqueMethods,
      datasets: [
        {
          label: "# of Tomatoes",
          data: uniqueOc,
          backgroundColor: [
            "rgba(255, 99, 132, 0.5)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(255, 206, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(255, 206, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(255, 159, 64, 0.2)",
            "rgba(255, 99, 132, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(255, 206, 86, 0.2)"
          ],
          borderColor: [
            "rgba(255,99,132,1)",
            "rgba(54, 162, 235, 1)",
            "rgba(255, 206, 86, 1)",
            "rgba(75, 192, 192, 1)",
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      //cutoutPercentage: 40,
      responsive: false,
    },
  });
  var ctx = document.getElementById("myChart1");
  var myChart = new Chart(ctx, {
    type: "pie",
    data: {
      labels: status.split(","),
      datasets: [
        {
          label: "# of Tomatoes",
          data: status_counter,
          backgroundColor: [
            "rgba(255, 99, 132, 0.5)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(255, 206, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(255, 206, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(255, 159, 64, 0.2)",
            "rgba(255, 99, 132, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(255, 206, 86, 0.2)"
          ],
          borderColor: [
            "rgba(255,99,132,1)",
            "rgba(54, 162, 235, 1)",
            "rgba(255, 206, 86, 1)",
            "rgba(75, 192, 192, 1)",
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      //cutoutPercentage: 40,
      responsive: false,
    },
  });
  var ctx = document.getElementById("myChart2").getContext("2d");
  var myChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: data.web_object_a_a,
      datasets: [
        {
          label: "Μέση Χρόνος Ζωής των web object",
          data: data.aver_life,
          backgroundColor: [
            "rgba(255, 99, 132, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(255, 206, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(255, 159, 64, 0.2)",
            "rgba(255, 99, 132, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(255, 206, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(255, 159, 64, 0.2)",
            "rgba(255, 99, 132, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(255, 206, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(255, 159, 64, 0.2)",
            "rgba(255, 99, 132, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(255, 206, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(255, 159, 64, 0.2)",
            "rgba(255, 99, 132, 0.2)",
          ],
          borderColor: [
            "rgba(255, 99, 132, 1)",
            "rgba(54, 162, 235, 1)",
            "rgba(255, 206, 86, 1)",
            "rgba(75, 192, 192, 1)",
            "rgba(153, 102, 255, 1)",
            "rgba(255, 159, 64, 1)",
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: false,
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
}

getData();
