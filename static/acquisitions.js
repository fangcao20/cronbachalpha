
(async function() {
  for (let i = 0; i < list_datasets.length; i++) {
    const dtsets = list_datasets[i];
    var datasets = [];
    for (let j = 0; j < dtsets.length; j++) {
      let dataset = {
        label: dtsets[j]['label'],
        data: dtsets[j]['data'],
        backgroundColor: dtsets[j]['backgroundColor'],
      };
      datasets.push(dataset);
    };
    var a = i + 1;
    var id = 'acquisitions-' + a;

    const labels = ['0', '1', '2', '3', '4'];
    const data = {
      labels: labels,
      datasets: datasets
    };

    new Chart(
      document.getElementById(id),
      {
        type: 'bar',
        data: data
      }
    );
  };
})();

  
  // console.log(list_datasets)
  // const labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'];
  // const data = {
  //   labels: labels,
  //   datasets: [{
  //     label: 'My First Dataset',
  //     data: [65, 59, 80, 81, 56, 55, 40],
  //     backgroundColor: [
  //       'rgba(255, 99, 132, 0.2)',
  //       'rgba(255, 159, 64, 0.2)',
  //       'rgba(255, 205, 86, 0.2)',
  //       'rgba(75, 192, 192, 0.2)',
  //       'rgba(54, 162, 235, 0.2)',
  //       'rgba(153, 102, 255, 0.2)',
  //       'rgba(201, 203, 207, 0.2)'
  //     ],
  //     borderColor: [
  //       'rgb(255, 99, 132)',
  //       'rgb(255, 159, 64)',
  //       'rgb(255, 205, 86)',
  //       'rgb(75, 192, 192)',
  //       'rgb(54, 162, 235)',
  //       'rgb(153, 102, 255)',
  //       'rgb(201, 203, 207)'
  //     ],
  //     borderWidth: 1
  //   },{
  //     label: 'My Second Dataset',
  //     data: [65, 59, 80, 81, 56, 55, 40],
  //     backgroundColor: [
  //       'rgba(255, 99, 132, 0.2)',
  //       'rgba(255, 159, 64, 0.2)',
  //       'rgba(255, 205, 86, 0.2)',
  //       'rgba(75, 192, 192, 0.2)',
  //       'rgba(54, 162, 235, 0.2)',
  //       'rgba(153, 102, 255, 0.2)',
  //       'rgba(201, 203, 207, 0.2)'
  //     ],
  //     borderColor: [
  //       'rgb(255, 99, 132)',
  //       'rgb(255, 159, 64)',
  //       'rgb(255, 205, 86)',
  //       'rgb(75, 192, 192)',
  //       'rgb(54, 162, 235)',
  //       'rgb(153, 102, 255)',
  //       'rgb(201, 203, 207)'
  //     ],
  //     borderWidth: 1
  //   }]
  // };


// })();