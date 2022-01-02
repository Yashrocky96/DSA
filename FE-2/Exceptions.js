// Explaining the usage of try catch in JS
function errorHandler(x) {
    try {
        const data = getX(x);
        return data;
    } catch(err) {
        return err;
    }
}

function getX(x) {
    if(x == 5) {
        return new Error("Error Occured");
    }
    return x;
}

// Driver Code

console.log(errorHandler(10));

// ---------------------------------------------------------------

// Usage of Throw to throw errors as needed

// This functions checks if a given string starts with alphabet or not
function checkAlphabet(X) {
	let n = X.charCodeAt(0);
	let strStartsWithALetter = (n>=65 && n < 91) || ( n>=97 && n<123);
// You can Google about what is ASCII code to know more about
	// why are we using numbers like 65, 91, 97 & 123

     if (strStartsWithALetter) {
     // Yes, it starts with an alphabet
     return true;
     } else {
     // No, it doesnt start with an alphabet
     return false;
     } 
}

function isAlphabet(X) {
     if (checkAlphabet(X)) {
          return "Yes";
     }
     else {
          throw "Not Alphabet";
     }
};
// Driver Code
console.log(isAlphabet("a"));