"""
Minimum difference btw two elements in any given arrays
"""

def minDiff(n, nums):
    nums.sort()
    min_diff = 1e9

    n = len(nums)
    for i in range(0, n-1):
        if nums[i + 1] - nums[i] < min_diff:
            min_diff = nums[i + 1] - nums[i]
    
    return min_diff


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    result = minDiff(n, nums)
    print(result)

if __name__=="__main__":
    main()