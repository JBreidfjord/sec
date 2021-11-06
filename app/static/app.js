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
      console.log(response);
    })
    .catch((error) => {
      console.error("Invalid file", error);
    });
};
