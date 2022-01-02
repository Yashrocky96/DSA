"""
Peak element is greater than both it's neighbours
"""

# Binary Seach function - tested
def binarySearch(arr, low, high):
    """
    General binarySearch algorithm iterative way to save space
    Fine tuning binarySearch according to this problem
    """
    while low <= high:
        mid = (low + high) // 2
        # Comparing mid elements neighbours
        try:
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] > arr[mid]:
                high = mid-1
            else:
                low = mid+1
        except:
            pass
    return -1

def peakElement(nums):
    n = len(nums)
    low, high = 0, n-1

    # Handling base cases
    try:
        if nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return n-1
    except: pass
    
    # Fine-Tuned Binary Search for this problem
    return binarySearch(nums, low, high)

def main():
    n = int(input())
    arr = input().split()
    arr = [int(i) for i in arr]
    print(peakElement(arr))

if __name__=="__main__":
    main()