"""
Understanding comparator old ways that is passed as key in 3.x
"""

def sortArrayAbsolute(n, nums):
    # Passes abs function once to all values I guess
    # Makes sorting easier this way
    nums = sorted(nums, key = abs)
    return nums

def main():
    n = int(input().strip())
    nums = list(map(int, input().strip().split(' ')))

    sortedArr = sortArrayAbsolute(n, nums)
    print(*sortedArr)

if __name__=="__main__":
    main()