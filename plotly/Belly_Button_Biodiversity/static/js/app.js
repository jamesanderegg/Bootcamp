function buildMetadata(thisSample) {


  // @TODO: Complete the following function that builds the metadata panel
  let url = "/metadata/" + thisSample;


  // Use d3 to select the panel with id of `#sample-metadata`
  let thisSelector = d3.select("#sample-metadata");
  // Use `.html("") to clear any existing metadata
  thisSelector.html("");
  // Use `Object.entries` to add each key and value pair to the panel

  // Use `d3.json` to fetch the metadata for a sample
  d3.json(url).then(function (response, error) {

    Object.entries(response).forEach(([key, value]) => {
      thisSelector.append("p").text(key + " " + value);


      // Hint: Inside the loop, you will need to use d3 to append new
      // tags for each key-value in the metadata.

      // BONUS: Build the Gauge Chart
      // buildGauge(data.WFREQ);
    });
  })
}

function buildCharts(sample) {

  url = "/samples/" + sample;
  // @TODO: Use `d3.json` to fetch the sample data for the plots
  
  // @TODO: Build a Bubble Chart using the sample data
  d3.json(url).then(function(response){
    //console.log(response)
    var trace1 = {
      x: response.otu_ids,
      y: response.sample_values,
      text: response.otu_labels,
      mode: 'markers',
      marker: {
        color: response.otu_ids,
        size: response.sample_values
      }
    };

    var data = [trace1];

    var layout = {
      title: 'Bubble Chart',
      showlegend: true,
      height: 600,
      width: 600
    };
    Plotly.newPlot('bubble', data, layout);
  })
  
  //buildPlot();
  // @TODO: Build a Pie Chart
  url = "/samples/" + sample;
  
  d3.json(url).then(function(response){
    console.log(response)
    var data = [{
      values: response.sample_values.slice(0,11),
      labels: response.otu_labels.slice(0,11),
      type: 'pie'
    }];
    
    var layout = {
      showlegend: false,
      height: 500,
      width: 500
    };
    
    Plotly.newPlot('pie', data, layout);
  });
  // HINT: You will need to use slice() to grab the top 10 sample_values,
  // otu_ids, and labels (10 each).
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {

      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
