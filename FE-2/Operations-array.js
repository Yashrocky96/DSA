// This function removes elements even duplicates from the arrays

function removeListedValues(arr, without) {
    for(let i = 0; i < without.length; i++) {
         while (arr.includes(without[i])) {
              const index = arr.indexOf(without[i]);
              if (index > -1) {
                   arr.splice(index, 1);
              }
         }
    }
    return arr
}

// Driver code
const arr = [1, 2, 2, 3, 1, 2]
const without = [2, 3]

console.log(removeListedValues(arr, without));

// ---------------------------------------------------------------------

function convertArray(arr) {
     let newArr = []
     arr.forEach((elem, i) => {
          newArr.push((i+1) * elem);
     });
     return newArr
}

// Driver Code
const arr = [1, 2, 2, 3, 1, 2];
console.log(convertArray(arr));

// ---------------------------------------------------------------------

// Checks if given number is a prime or not
function isPrime(n) {
     if(n == 0 || n == 1) {
         return false;
     }
     for(let i = 2 ; i*i <= n ; i++) {
         if(n % i == 0) {
             return false;
         }
     }
     return true;
 }
 
 // modifies arrays based on prime numbers
 let modify = (array) => {
     array.forEach((elem, i) => {
         if (isPrime(elem)) {
             array[i] += 1;
         } else {
             array[i] *= 2;
         }
     });
     return array;
 }
 
 // Driver Code
 const arr = [1, 2, 3, 4, 5];
 console.log(modify(arr));