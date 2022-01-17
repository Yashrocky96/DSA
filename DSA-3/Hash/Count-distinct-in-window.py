"""
using maps and moving windows we get distinct elements in a window
"""

from collections import Counter

"""
Use this to get the count in the window len(Counter(arr))
This doesn't pass perf tests as we are calculating Counter
for all windows, this works I just forgot the base condition
"""

def countDistinctElements(n, b, arr):
    # Base condition
    if b > n:
        return []
    # Hash map of first window and it's distinct count
    mp = Counter(arr[:b])
    res = [len(mp)]

    # loop till the last possible window value
    for i in range(1, n - b+1):
        # Sliding window values
        l, r = i - 1 , i - 1 + b
        # Decrease or remove from map the left value
        mp[arr[l]] -= 1
        if mp[arr[l]] == 0:
            mp.pop(arr[l])
        # Increase or insert into map the right most of window
        if arr[r] in mp:
            mp[arr[r]] += 1
        else:
            mp[arr[r]] = 1
        # add distinct count of values
        res.append(len(mp))
    return res

def main():
    n, b = list(map(int, input().strip().split(' ')))
    arr = list(map(int, input().strip().split(' ')))

    result = countDistinctElements(n, b, arr)
    print(*result)

if __name__=="__main__":
    main()