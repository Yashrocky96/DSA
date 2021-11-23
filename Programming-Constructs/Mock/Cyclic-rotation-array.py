"""
This performs a cyclic rotation of array by a given number of times
"""

def cyclicRotation(arr, n, k):
    for i in range(k):
        arr.insert(0, arr[n-1])
        arr.pop()
    return arr

# NOTE: Please do not modify this function
def main():
    n = int(input())
    arr = list(map(int, input().strip().split(' ')))
    k = int(input())

    rotatedArr = cyclicRotation(arr, n, k)

    print(*rotatedArr)


if __name__ == "__main__":
    main()
