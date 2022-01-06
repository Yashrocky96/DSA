"""
Given a matrix we can find the kth smallest number in this easy way
"""

# This function gets the rank, number of k small elements
def rank(matrix, mid):
    count, n = 0, len(matrix)
    i, j= n - 1, 0

    while i >= 0 and j < n:
        if matrix[i][j] > mid:
            i -= 1
        else:
            count += i + 1
            j += 1
    return count

def kthSmallestElementInMatrix(matrix, k):
    low = matrix[0][0]
    high = matrix[-1][-1]
    ans = 0

    while low <= high:
        mid = (low + high) // 2
        
        # Get Rank of mid
        element = rank(matrix, mid)

        if element >= k:
            ans = mid
            high = mid-1
        else:
            low = mid + 1
    return ans

def main():
	n , k = map(int,input().split())
	matrix = [list(map(int,input().split())) for i in range(n)]
	ans = kthSmallestElementInMatrix(matrix , k)
	print(ans)

if __name__=="__main__":
	main()