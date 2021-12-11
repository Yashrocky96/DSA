"""
Traverses matrix in spiral order
1 2 3
8 9 4
7 6 5
"""

def spiralMatrixII(n):
    # initialized Matrix [[0]*n]*n creates references instead of initialization
    M = [[0 for i in range(0,n)] for j in range(0,n)]
    k, l, m = 0, 0, n
    
    val = 1
    # Create four boundaries and push them down when traversed
    while k < m and l < n:
        for i in range(l, n):
            # print("({}, {})".format(k ,i), end = " ")
            M[k][i] += val
            # print(M[k][i])
            val += 1
        k += 1
        
        for i in range(k, m):
            # print("({}, {})".format(i ,n-1), end = " ")
            M[i][n-1] += val
            # print(M[i][n-1])
            val += 1
        n -= 1
        
        if k < m:
            for i in range(n-1, l-1, -1):
                # print("({}, {})".format(m-1 ,i), end = " ")
                M[m-1][i] = val
                # print(M[m-1][i])
                val += 1
            m -= 1
        
        if l < n:
            for i in range(m-1, k-1, -1):
                # print("({}, {})".format(i, l), end = " ")
                M[i][l] = val
                # print(M[i][l])
                val += 1
            l += 1
    return M

def main():
    n = int(input())
    matrix = spiralMatrixII(n)
    for row in matrix:
        print(*row)

if __name__=="__main__":
    main()
