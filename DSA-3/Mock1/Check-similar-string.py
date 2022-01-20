"""
This checks if the given strings are similar or not 
when k most frequency difference is considered
"""

from collections import Counter

def similarString(n, m, k, s1, s2) -> str:
    count1 = Counter(s1)
    count2 = Counter(s2)

    # Check in s1 string first
    for i in count1:
        if abs(count1[i] - count2[i]) <= k:
            pass
        else: 
            return "No"
    # if any characters frequency doesn't match in either we return
    for i in count2:
        if abs(count1[i] - count2[i]) <= k:
            pass
        else: 
            return "No"

    return "Yes"

def main():
    testcases = int(input())
    for _ in range(testcases):
        n, m, k = map(int, input().split())
        s1, s2 = input(), input()
        ans = similarString(n, m, k, s1, s2)
        print(ans)

if __name__=="__main__":
    main()