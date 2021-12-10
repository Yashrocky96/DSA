"""
Given a matrix, element position, direction to move and number of steps
We use the function to get the traversal path values to the end position
whilst -1 if wrong path given
"""


def matrixTraversal(matrix, row, col, dirToMove, stepsToMove):
    res = []

    try:
        for i in range(stepsToMove):
            if dirToMove == 1:
                col += 1
            elif dirToMove == 2:
                row += 1
            elif dirToMove == 3:
                col -= 1
            else:
                row -= 1
            res.append(matrix[row][col])
    except IndexError:
        return [-1]
    return res

if __name__ == '__main__':
    row = input().split()
    n = int(row[0])
    m = int(row[1])
    grid = []
    for i in range(n):
        nums = input().split()
        nums = [int(i) for i in nums]
        grid.append(nums)

    position = input().split()
    currPosX = int(position[0])
    currPosY = int(position[1])
    move = input().split()
    dirToMove = int(move[0])
    stepsToMove = int(move[1])

    result = matrixTraversal(grid, currPosX, currPosY, dirToMove, stepsToMove)
    for res in result:
        print(res,end =" ")
