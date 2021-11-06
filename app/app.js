


document.getElementById("file_submit").onclick = async function() {
    var csv_file = document.getElementById("file_input").files[0];
    // const rawData = await csv_file.text();

    // let data_array = rawData.split("\r\n");
    // let header = data_array[0].split(",");
    // let rows = data_array.length;
    // let cols = header.length;
    // let jsonData = [];

    // for(i=1; i <rows-1; i++) {
    //     let obj = {};
    //     let myNewLine = data_array[i].split(",");
    //     for (j=0; j < cols; j++) {
    //         obj[header[j]] = myNewLine[j];
    //     };
    //     jsonData.push(obj)
    // };

    // document.getElementById("csv").innerHTML = data_array;
    // console.log(jsonData);
    // console.table(jsonData);
    console.log(csv_file)
}