# Implemented max element search 
def maxInArray(n, arr):
    max = 0
    for i in range(n):
        if max < arr[i]:
            max = arr[i]

    return max

# NOTE: Please do not modify this function
def main():
    n = int(input())
    arr = list(map(int, input().strip().split(' ')))

    maxVal = maxInArray(n, arr)
    print(maxVal)


if __name__ == "__main__":
    main()
