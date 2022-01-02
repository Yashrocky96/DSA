// Using Map in Js to map data and create new array
function findLength(arr) {
    arr = arr.map((str) => {
        if (str) {
            return str.length;
        } else {
            return 0;
        }
    });
    return arr;
}
// Driver Code
console.log(findLength(["hello","world"]));

// ------------------------------------------------

// Using Filter to filter data
function filterByCity(arr) {
    let filtered = arr.filter(data => {
         let city = data.city.toLowerCase();

         return city === "bangalore" || 
         city === "hyderabad"
         });  

    return filtered;
}

console.log(filterByCity([{name: "Rachel", city: "bangalore" }]));