"""
Implementing Linear Search using arrays
"""

def findElement(n, arr, x):
    """
    Loop through the array and check each value
    if equals to x and get the index position for the
    left-most value found in the array
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# NOTE: Please do not modify this function
def main():
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    x = int(input().strip())

    xIndex = findElement(n, arr, x)
    print(xIndex)

if __name__=="__main__":
    main()
