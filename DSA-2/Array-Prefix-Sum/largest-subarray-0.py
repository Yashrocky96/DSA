"""
Finds the largest subarray and returns that subarray
"""

def largestSubarraySumZero(n, arr):
    prefix = 0
    max_len = -1
    mp = {}

    for i in range(n):
        # Prefix sum variable
        prefix += arr[i]
        # if 0 we found subarray with sum 0
        if prefix == 0:
            max_len = i+1
            start = 0
            end = i
        # if found in map, first iter we found our length
        # and following iter we get the max_len
        if prefix in mp:
            length = i - mp[prefix]
            if length > max_len:
                max_len = length
                start = mp[prefix] + 1
                end = i
        # enter sum, index into map
        else:
            mp[prefix] = i
    
    if max_len == -1:
        return [-1]

    return arr[start:end+1]

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = largestSubarraySumZero(n, arr)
    print(*result)

if __name__=="__main__":
    main()