"""
Given string sort using count frequencies
"""

from collections import Counter

def countSort(n, s):
    count = Counter(s)
    # count.sorted()
    # print(count)
    res = ""
    for code in range(ord('a'), ord('z') + 1):
        alpha = chr(code)
        res += alpha * count[alpha]
    # for i in count:
    
    return res

def main():
    n = int(input())
    s = input()
    result = countSort(n, s)
    print(result)

if __name__=="__main__":
    main()