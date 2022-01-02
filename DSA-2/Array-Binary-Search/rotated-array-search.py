"""
Implementing search in a given sorted rotated array
"""

# Binary Seach function - tested
def binarySearch(arr, low, high, target):
    """
    General binarySearch algorithm iterative way to save space
    """
    while low <= high:
        mid = (low + high) // 2
        # print("Target: {}".format(target))
        # print("Bs-Mid: {}".format(mid))
        # ignore left half
        if arr[mid] < target:
            low = mid + 1
        # ignore right half
        elif arr[mid] > target:
            high = mid-1
        # target found at mid index
        else:
            return mid
    return -1

# Finding pivot
def pivot(arr):
    n = len(arr)
    low, high = 0, n-1

    while low <= high:
        mid = (low + high)//2
        # Base conditions
        try:
            if arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid] < arr[mid - 1]:
                return mid-1
        except:
            pass
        # Search left
        if arr[mid] <= arr[0]:
            high = mid-1
        #       Search right
        elif arr[mid] > arr[0]:
            low = mid + 1
    
    # No pivot present
    return -1

# SearchInRotatedSortedArray solution
def findInRotatedArray(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    ans = -1
    n = len(nums)
    p = pivot(nums)

    if p == -1:
        ans = binarySearch(nums, 0, n-1, target)
    elif nums[p] == target:
        return p
    # Right part of pivot
    elif nums[0] > target:
        ans = binarySearch(nums, p+1, n-1, target)
    # Left side of pivot
    else:
        ans = binarySearch(nums, 0, p-1, target)
    
    return ans

if __name__ == '__main__':
    n = int(input().strip())
    nums = [int(i) for i in input().strip().split()]
    q = int(input().strip())

    for i in range(q):
        target = int(input().strip())
        print(findInRotatedArray(nums, target))