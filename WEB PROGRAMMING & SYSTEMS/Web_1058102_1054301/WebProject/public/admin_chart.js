const button = document.getElementById("submit");
button.addEventListener("click", async (event) => {
  var day = document.getElementById("day").value;
  var method = document.getElementById("method").value;
  var company = document.getElementById("company").value;
  var content = document.getElementById("content").value;

  console.log(day);
  console.log(method);
  console.log(company);
  console.log(content);
  async function getData() {
    const response = await fetch("/morf_chart/1");
    const data = await response.json();
    var data_chart = [];
    const data_00 = [];
    const data_01 = [];
    const data_02 = [];
    const data_03 = [];
    const data_04 = [];
    const data_05 = [];
    const data_06 = [];
    const data_07 = [];
    const data_08 = [];
    const data_09 = [];
    const data_10 = [];
    const data_11 = [];
    const data_12 = [];
    const data_13 = [];
    const data_14 = [];
    const data_15 = [];
    const data_16 = [];
    const data_17 = [];
    const data_18 = [];
    const data_19 = [];
    const data_20 = [];
    const data_21 = [];
    const data_22 = [];
    const data_23 = [];

    data_td = data.td_final;
    console.log(data_td);
    data_length = data.td_final.length;
    var methods = [];
    var days = [];
    var contents = [];

    unique_response = data_td[0].unique_response_content_type;
    console.log(unique_response);
    unique_method = data_td[0].unique_method;
    var dion = 9;

    if (parseInt(day) == dion) {
      days = [1, 2, 3, 4, 5, 6, 7];
    } else {
      days = [day];
    }
    if (method == 91) {
      methods = unique_method;
    } else {
      methods = [method];
    }
    if (content == 911) {
      contents = unique_response;
    } else {
      contents.push(content);
    }
    //console.log(contents[0]);

    for (let m = 0; m < contents.length; m++) {
      for (let j = 0; j < methods.length; j++) {
        for (let k = 0; k < days.length; k++) {
          for (let i = 0; i < data_td.length; i++) {
            mera_final = data_td[i].day;
            method_final = data_td[i].method;
            timing_final = parseFloat(data_td[i].timing);
            time_final = data_td[i].time;
            content_final = data_td[i].content_type;
            //console.log(mera_final, method_final, content_final);
            if (
              mera_final == days[k] &&
              method_final == methods[j] &&
              content_final == contents[m]
            ) {
              //console.log("poutsa");
              //console.log(mera_final, method_final, content_final);
              console.log(mera_final);
              console.log(method_final);
              console.log(content_final);
              console.log(time_final);
              console.log(timing_final);
              if (time_final == "00") {
                data_00.push(timing_final);
              } else if (time_final == "01") {
                data_01.push(timing_final);
              } else if (time_final == "02") {
                data_02.push(timing_final);
              } else if (time_final == "03") {
                data_03.push(timing_final);
              } else if (time_final == "04") {
                data_04.push(timing_final);
              } else if (time_final == "05") {
                data_05.push(timing_final);
              } else if (time_final == "06") {
                data_06.push(timing_final);
              } else if (time_final == "07") {
                data_07.push(timing_final);
              } else if (time_final == "08") {
                data_08.push(timing_final);
              } else if (time_final == "09") {
                data_09.push(timing_final);
              } else if (time_final == "10") {
                data_10.push(timing_final);
              } else if (time_final == "11") {
                data_11.push(timing_final);
              } else if (time_final == "12") {
                data_12.push(timing_final);
              } else if (time_final == "13") {
                data_13.push(timing_final);
              } else if (time_final == "14") {
                data_14.push(timing_final);
              } else if (time_final == "15") {
                data_15.push(timing_final);
              } else if (time_final == "16") {
                data_16.push(timing_final);
              } else if (time_final == "17") {
                data_17.push(timing_final);
              } else if (time_final == "18") {
                data_18.push(timing_final);
              } else if (time_final == "19") {
                data_19.push(timing_final);
              } else if (time_final == "20") {
                data_20.push(timing_final);
              } else if (time_final == "21") {
                data_21.push(timing_final);
              } else if (time_final == "22") {
                data_20.push(timing_final);
              } else if (time_final == "23") {
                data_21.push(timing_final);
              }
            }
          }
        }
      }
    }

    data_chart = [
      data_00,
      data_01,
      data_02,
      data_02,
      data_03,
      data_04,
      data_04,
      data_05,
      data_06,
      data_07,
      data_08,
      data_09,
      data_10,
      data_11,
      data_12,
      data_13,
      data_14,
      data_15,
      data_16,
      data_17,
      data_18,
      data_19,
      data_20,
      data_21,
      data_22,
      data_23,
    ];
    //console.log("auto einai to data chart");
    //console.log(data_chart);
    var meso_geniko = [];

    for (let i = 0; i < data_chart.length; i++) {
      var mesa_data_chart = data_chart[i];
      let result = 0;
      let m_g = 0;
      for (let k = 0; k < mesa_data_chart.length; k++) {
        result += mesa_data_chart[k];
        m_g = result / mesa_data_chart.length;
        //console.log(result);
        //meso_geniko.push(result);
      }
      meso_geniko.push(m_g);
    }
    console.log(meso_geniko);

    var ctx = document.getElementById("myChart").getContext("2d");
    var myChart = new Chart(ctx, {
      type: "bar",
      data: {
        labels: [
          "1 π.μ.",
          "2 π.μ.",
          "3 π.μ.",
          "4 π.μ.",
          "5 π.μ.",
          "6 π.μ.",
          "7 π.μ.",
          "8 π.μ.",
          "9 π.μ.",
          "10 π.μ.",
          "11 π.μ.",
          "12 π.μ.",
          "1 μ.μ.",
          "2 μ.μ.",
          "3 μ.μ.",
          "4 μ.μ.",
          "5 μ.μ.",
          "6 μ.μ.",
          "7 μ.μ.",
          "8 μ.μ.",
          "9 μ.μ.",
          "10 μ.μ.",
          "11 μ.μ.",
          "12 μ.μ.",
        ],
        datasets: [
          {
            label: "Μέση Χρονική απόκριση",
            data: meso_geniko,
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
});
