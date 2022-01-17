// Reverse, check if palindrome or convert a string into palindrome

class WordKit {
    reverse(str) {
         return (str.split("").reverse().join(""));
    }
    isPalindrome(str) {
         if (str === this.reverse(str)) return true
         else return false
    }
    makePalindrome(str) {
         if (this.isPalindrome(str)) return str
         else return str + this.reverse(str);
    }
}

module.exports = WordKit;