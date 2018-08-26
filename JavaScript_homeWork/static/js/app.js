//Pass in the data
var tableData = data;

//Filter button and Input Selection
//Filter button I don't use currently
var filterButton = d3.select("#filter-btn");
var inputElement = d3.select("#myInput");

//appending a class table-striped in the tbody is the hoover effect on the rows
var table_body = d3.select("tbody");
table_body.attr("class", "table table-striped")

//After data is filtered and concated I remove duplicates
function removeDuplicates(arr){
    let unique_array = []
    for(let i = 0;i < arr.length; i++){
        if(unique_array.indexOf(arr[i]) == -1){
            unique_array.push(arr[i])
        }
    }
    return unique_array
}
//Renders table to screen
function myFunction(this_data){
    this_data.forEach(x => {
        let tb = table_body.append('tr')
        Object.entries(x).forEach(([key, value]) => {
            tb.append('td').text(value)

        })
    })
    
}
//event listener on KEY UP
inputElement.on("keyup", function(){
    inputValue = inputElement.property("value")
    if(inputValue == 0){
        //Make sure we still print table when input box is 0
        d3.select('tbody').selectAll('tr').remove();
        myFunction(tableData);
        console.log('reset');
    }else{
        //Delete old table but leave the class element
        d3.select('tbody').selectAll('tr').remove();

        //filter through each column or key in object.
        //Need to make this dynamic
        //for each.... or maybe iterate through object with integers
        filterDates = tableData.filter(tableData => tableData.datetime.indexOf(inputValue) >= 0 ? true : false);
        console.log("Date filter: ",filterDates.length);
        
        filterCity = tableData.filter(tableData => tableData.city.indexOf(inputValue) >= 0 ? true : false);
        console.log("City filter: ",filterCity.length);
        
        filterState = tableData.filter(tableData => tableData.state.indexOf(inputValue) >= 0 ? true : false);
        console.log("State filter: ",filterState.length);

        filterCountry = tableData.filter(tableData => tableData.country.indexOf(inputValue) >= 0 ? true : false);
        console.log("Country filter: ",filterCountry.length);

        filterShape = tableData.filter(tableData => tableData.shape.indexOf(inputValue) >= 0 ? true : false);
        console.log("Shape filter: ",filterShape.length);

//  COULD NOT SORT ON DURATION . COULD NOT FIGURE IT OUT
//        filterShape = tableData.filter(tableData => tableData.durationMinutes.indexOf(inputValue) >= 0 ? true : false);
//        console.log("Shape filter: ",filterShape.length);

        filterComments = tableData.filter(tableData => tableData.comments.indexOf(inputValue) >= 0 ? true : false);
        console.log("Comments filter: ",filterComments.length);

        //concat and then remove duplicates
        let combined_filter = removeDuplicates(filterDates.concat(filterCity, filterState, filterCountry, filterShape, filterComments))
        
        //Sort the table
        combined_filter = combined_filter.sort(function(a,b){
            console.log("A",a)
            console.log("B",b)
            return new Date(a.datetime) - new Date(b.datetime);
          });

        //print filtered table
        myFunction(combined_filter)
    }
    
})

//Very first thing print whole table
myFunction(tableData)


