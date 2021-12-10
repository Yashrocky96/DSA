"""
Check String permutations of a given string forms a palindrome or not
We check if more than one character has odd frequency then palindrome
of all permutations isn't possible for the string   
"""

from collections import Counter

def isPermutationPalindrome(s):
    n = len(s)
    res = Counter(s)
    count = 0
    for i in res:
        if res[i] % 2 != 0:
            count += 1
        if count > 1:
            return False      
    return True

T = int(input())
for _t in range(T):
    s = input().strip()
    result = isPermutationPalindrome(s)
    print(result)