"""
Sorting array in wave fashion
"""

def wiggleSort(nums):
    # nums.sort()

    # mid = len(nums) // 2
    for i in range(1, len(nums), 2):
        if nums[i] < nums[i-1]:
            nums[i], nums[i-1] = nums[i-1], nums[i]
        try:
            if nums[i] < nums[i + 1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        except:
            pass

        # nums[i], nums[mid + i] = nums[mid+i], nums[i]

    return nums

def main():
    n = int(input().strip())
    nums = list(map(int,input().strip().split()))

    ans = wiggleSort(nums)
    print(*ans)

if __name__=="__main__":
    main()