"""
Given a string we get the number of characters to be used
to form the longest possible palindrome from it
"""

from collections import Counter

def longestPalindrome(n, s):
    ans = 0
    mp = Counter(s)
    for i in mp:
        # adds all 2s and changes to remainders
        if mp[i] % 2 == 0:
            ans += mp[i]
        elif mp[i] > 0:
            ans += mp[i] - 1
        mp[i] %= 2
    # ternary operator checks if 1 is there in map
    ans += 1 if 1 in mp.values() else 0

    return ans

def main():
    n = int(input())
    s = input()
    result = longestPalindrome(n, s)
    print(result)

if __name__=="__main__":
    main()