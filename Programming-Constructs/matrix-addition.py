""" 
Addition of matrix using list comprehensions
List comprehensions save hassle of declaring matrix
"""
def additionOfMatrix(n, m, matrixOne, matrixTwo):
    matrix = [[matrixOne[i][j] + matrixTwo[i][j] for j in range(m)]
                    for i in range(n)]
    return matrix

# NOTE: Please do not modify this function
def main():
    n, m = map(int, input().split(' '))

    matrixOne = []
    matrixTwo = []

    for i in range(n):
        row = list(map(int, input().split(' ')))
        matrixOne.append(row)

    for i in range(n):
        row = list(map(int, input().split(' ')))
        matrixTwo.append(row)

    sumMatrix = additionOfMatrix(n, m, matrixOne, matrixTwo)

    for i in sumMatrix:
        print(*i)

if __name__=="__main__":
    main()
