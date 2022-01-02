"""
In sorted array finding the first 1 using binary search
"""

def zeroOnes(n, arr):
    low = 0
    high = n-1

    while low <= high:
        # base condition
        mid = int((low + high) / 2)

        if arr[mid] == 1 and (mid == 0 or arr[mid - 1] == 0):
            return mid

        # Search right
        elif arr[mid] == 1:
            high = mid-1
        # Search left
        else:
            low = mid + 1
    
    return -1

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = zeroOnes(n, arr)
    print(result)

if __name__=="__main__":
    main()