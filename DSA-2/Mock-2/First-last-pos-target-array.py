"""
given target to find we determine the first and last position of the target
"""
# Binary Seach function - tested
def binarySearch(arr, key):
    """
    General binarySearch algorithm iterative way to save space
    Fine tuning binarySearch according to this problem
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        # base condition
        mid = int((low + high) / 2)
        if arr[mid] == key:
            # Found left most position of key
            if mid == 0:
                return mid
            elif arr[mid - 1] < key:
                return mid
            else:
                high = mid-1    

        # Search left
        elif arr[mid] > key:
            high = mid-1
        # Search right
        else:
            low = mid + 1
    return -1

def rightBS(arr, key, low):
    high = len(arr) - 1
    while low <= high:
        # base condition
        mid = int((low + high) / 2)
        if arr[mid] == key:
            # Found left most position of key
            if mid == high:
                return mid
            elif arr[mid + 1] > key:
                return mid
            else:
                low = mid + 1    

        # Search left
        elif arr[mid] > key:
            high = mid-1
        # Search right
        else:
            low = mid + 1
    return -1


class Solution:
    def findFirstAndLastPositionOfElementInSortedArray(self, nums, target):
        
        first = binarySearch(nums, target)
        last = rightBS(nums, target, first)

        ans = [first, last]

        return ans