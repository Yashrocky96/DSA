// Finding permutations and combinations

class Combinatorics {
    constructor (n, r) {
         this.n = n;
         this.r = r;
         this.factorial = (num) => {
              if (this.n == 1 || num == 0) {
                   return 1
              } return num * this.factorial(num-1)
         }
    }

    findPermutations(N, R) {
         if (R < N) {
              return Math.floor(this.factorial(N) / this.factorial(N-R))
         } else return 0
    }

    findCombinations(N, R) {
         if (R < N) {
              return Math.floor(this.factorial(N) / 
                   (this.factorial(R) * this.factorial(N-R)))
         } else return 0
    }
}

module.exports = Combinatorics;