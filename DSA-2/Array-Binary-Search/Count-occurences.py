"""
Count occurences of a given number in a sorted array
"""

# Binary Seach function -- tested
def binarySearchFirst(arr, low, high, k):
    """
    General binarySearch algorithm iterative way to save space
    Fine tuning binarySearch according to this problem
    """
    while low <= high:
        mid = (low + high) // 2
        # find first occurence
        if arr[mid] == k:
            try:
                if low == high:
                    return mid
                if arr[mid] > arr[mid-1] or mid == 0:
                    return mid
                else:
                    high = mid - 1
            except:
                pass
        elif arr[mid] > k:
            high = mid - 1
        elif arr[mid] < k:
            low = mid + 1
    return -1

def binarySearchLast(arr, low, high, k):
    """
    General binarySearch algorithm iterative way to save space
    Fine tuning binarySearch according to this problem
    """
    while low <= high:
        mid = (low + high) // 2
        # find last occurence
        if arr[mid] == k:
            try:
                if low == high:
                    return mid
                if arr[mid] < arr[mid+1] or mid == (len(arr) - 1):
                    return mid
                else:
                    low = mid + 1
            except:
                pass
        elif arr[mid] > k:
            high = mid - 1
        elif arr[mid] < k:
            low = mid + 1
    return -1

def countOccurrences(n, arr, k):
    """
    Fine-Tuning Binary Search to Counting number of occurences
    """
    low, high = 0, n-1
    # print("low, high: {} {}".format(low, high))
    first = binarySearchFirst(arr, low, high, k)
    last = binarySearchLast(arr, low, high, k)

    if first == -1:
        return 0
    
    return last-first+1

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = countOccurrences(n, arr, k)
    print(result)

if __name__=="__main__":
    main()