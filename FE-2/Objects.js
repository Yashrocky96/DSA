// Creating objects in JS or Json way

function personDetail(a, b) {
    const obj=  {
         firstName: a,
         lastName: b,
         fullName: a + " " + b 
    }
    return obj
}
// Driver Code
console.log(personDetail("Yash", "Agarwal"));

// ---------------------------------------------------------------

// Given date in dd/mm/yyyy format this function returns number of days
// between today and given date
function getNumberOfDays(date) {
    date = date.split("/");

    dd = parseInt(date[0]);
    mm = parseInt(date[1]);
    yyyy = parseInt(date[2]);

    const dateObj = new Date(yyyy, mm-1, dd);
    const today = new Date();

    let msdiff =  today.getTime() - dateObj.getTime();
    let daydiff = msdiff / (1000 * 60 * 60 * 24);

    return parseInt(daydiff);
}

console.log(getNumberOfDays("25/12/2021"));