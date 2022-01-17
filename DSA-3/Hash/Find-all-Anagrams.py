"""
Calculating or using Counter on all windows is inefficient
than removing one before and adding in the window
"""

from collections import Counter

def find_anagrams(p, s):
    res = []
    # b is the window of pattern p
    b, n = len(p), len(s)
    # Hash map of pattern to be matched with all windows
    pattern = Counter(p)
    mp = Counter(s[:b])
    if mp == pattern:
        res = [0]
    
    for i in range(1, n - b+1):
        # Sliding window gives O(N)
        l, r = i - 1, i - 1 + b

        mp[s[l]] -= 1
        if mp[s[l]] == 0:
            mp.pop(s[l])
        # Increase or insert into map the right most of window
        if s[r] in mp:
            mp[s[r]] += 1
        else:
            mp[s[r]] = 1

        # if Counter or maps matches the pattern hash map
        if mp == pattern:
           res.append(i)
    return res

def main():
    s, p = input().split()
    answer = find_anagrams(p, s)
    print(len(answer))
    print(' '.join([str(i) for i in answer]))

if __name__ == "__main__":
    main()