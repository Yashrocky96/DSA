"""
Find sum of pairs matching the given target
"""

def twoSumInSortedArray(n, nums, target) -> bool:
    l, r = 0, n-1

    while l < r:
        check = nums[l] + nums[r]

        if check < target:
            l += 1
        elif check > target:
            r -= 1
        else:
            return True
    return False

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    target = int(input())
    result = twoSumInSortedArray(n, nums, target)
    if result:
        print("Present")
    else:
        print("Not Present")

if __name__=="__main__":
    main()