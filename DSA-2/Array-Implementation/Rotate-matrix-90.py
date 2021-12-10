"""
Rotate Matrix 90degrees Only function matters here
"""

from crio.io import PrintMatrix

class Solution:
    def __init__(self, matrix):
        self.matrix = matrix

    def rotateImage(self):
        N = len(self.matrix[0])
        for i in range(N//2):
            for j in range(i, N-i-1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[N-1-j][i]
                matrix[N-1-j][i] = matrix[N-1-i][N-1-j]
                matrix[N-1-i][N-1-j] = matrix[j][N-1-i]
                matrix[j][N-1-i] = temp

if __name__ == '__main__':
    n = int(input())
    matrix = []
    for i in range(n):
        nums = input().split()
        nums = [int(i) for i in nums]
        matrix.append(nums)
    sol = Solution(matrix)
    sol.rotateImage()
    PrintMatrix.SquareMatrix(sol.matrix)