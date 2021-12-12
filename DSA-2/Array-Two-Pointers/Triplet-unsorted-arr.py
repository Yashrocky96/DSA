"""
Given unsorted array find max sum of triplet
Here TC: O(N square) because of 2 Nesting level
instead of 3 in brute force approach
"""

def maxSumTriplet(n: int, arr: list):
    sm = 0
    # Middle element loops
    for j in range(1, n-1):
        max1 = max2 = 0
        # i and k loops find max before and after less and greater than j
        for i in range(0, j):
            if arr[i] < arr[j] and arr[i] > max1:
                max1 = arr[i]
        for k in range(j+1, n):
            if arr[k] > arr[j] and arr[k] > max2:
                max2 = arr[k]

        # This condition gets the sum that is the maximum of all
        if max1 > 0 and max2 > 0:
            if max1 + arr[j] + max2 > sm:
                sm = max1 + arr[j] + max2
    return sm

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        ans = maxSumTriplet(n, arr)
        print(ans)

if __name__=="__main__":
    main()