document.getElementById("file_submit").onclick = async function () {
  formData = new FormData();
  formData.append("data_file", document.getElementById("file_input").files[0]);
  fetch("/", { method: "POST", body: formData })
    .then((response) => {
      if (!response.ok) {
        throw new Error(response.statusText);
      }
      return response.json();
    })
    .then((response) => {
      data = JSON.parse(response);
      chartData(data);
    })
    .catch((error) => {
      console.error("Invalid file", error);
    });
};

function chartData(data) {
  var ctx = document.getElementById("predictions");
  const myChart = new Chart(ctx, {
    type: "bar",
    data: {
      datasets: [
        {
          label: "# of Patients with Diabetes",
          data: data,
          backgroundColor: [
            "rgba(255, 99, 132, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(255, 206, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(255, 159, 64, 0.2)",
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
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
}
