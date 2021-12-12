"""
Remove duplicates from an array where there can be not more than two of them    
"""

def removeDuplicatesFromSortedArrayII(n, nums):
    i = j = 0
    while i < len(nums):
        t = 0
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
                t += 1
            else: 
                break
        k = j
        if t > 1:
            nums = nums[:(i+2)] + nums[k:]
            i += 1
            j = i
        else:
            i += 1
            j = i
    return [len(nums), nums]


def main():
    n = int(input().strip())
    nums = list(map(int, input().strip().split(' ')))

    length, newNums = removeDuplicatesFromSortedArrayII(n, nums)
    print(length)
    print(*newNums)

if __name__=="__main__":
    main()