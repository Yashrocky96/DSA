"""
Calculating sum of principal diagonal of the matrix
"""
def diagonalSum(matrix, n):
    sum = 0
    for i in range(n):
        sum += matrix[i][i]
    return sum

# NOTE: Please do not modify this function
def main():
    n = int(input())

    matrix = []

    for i in range(0, n):
        row = list(map(int, input().strip().split(' ')))
        matrix.append(row)

    ans = diagonalSum(matrix, n)
    print(ans)


if __name__ == "__main__":
    main()
