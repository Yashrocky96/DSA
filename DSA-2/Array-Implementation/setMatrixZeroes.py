def setMatrixZeroes(grid):
    row = len(grid)
    col = len(grid[0])
    r, c = [], []

    # loop through matrix and flag the rows and cols to turn to 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 0:
                r.append(i)
                c.append(j)

    """
    Two loops converts all the rows and cols that are flagged
    to 0
    """
    for i in r:
        for j in range(col):
            grid[i][j] = 0
    for j in c:
        for i in range(row):
            grid[i][j] = 0

    return grid

if __name__ == '__main__':
    row = input().split()
    m = int(row[0])
    n = int(row[1])
    grid = []
    for i in range(m):
        nums = input().split()
        nums = [int(i) for i in nums]
        grid.append(nums)
    setMatrixZeroes(grid)
    for row in grid:
        print(*row)