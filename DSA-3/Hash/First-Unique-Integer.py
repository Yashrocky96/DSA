"""
Using counter these problems are becoming simple
"""

from collections import Counter

def firstUniqueInteger(lis):
    mp = Counter(lis)
    for i in mp:
        if mp[i] == 1:
            return i
    return -1

def main():
    n = int(input())
    lis = list(map(int,input().split()))
    assert len(lis) == n
    result = firstUniqueInteger(lis)
    print(result)

if __name__ == "__main__":
    main()