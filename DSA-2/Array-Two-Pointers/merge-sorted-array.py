"""
Given two arrays merge both into one
"""

# from crio.io import PrintMatrix

def mergeSortedArray(nums1, len1, nums2, len2):
    i, j, res = 0, 0, []
    
    # Reach min length and merge based on values
    while i < len1 and j < len2:
        if nums1[i] <= nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1
    # Append remaining elements from min to max length
    while i < len1:
        res.append(nums1[i])
        i += 1
    while j < len2:
        res.append(nums2[j])
        j += 1

    return res

if __name__ == '__main__':
    m = int(input())
    n = int(input())
    nums1 = input().split()
    nums1 = [int(i) for i in nums1]
    nums2 = input().split()
    nums2 = [int(i) for i in nums2]
    res = mergeSortedArray(nums1, len(nums1), nums2, len(nums2))
    # PrintMatrix.OneDMatrix(res, " ")