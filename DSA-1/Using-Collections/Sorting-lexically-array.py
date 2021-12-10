"""
Sorting an array of strings in lexicographical order
"""

def sortArray(n, arr):
    return sorted(arr)

# NOTE: Please do not modify this function
def main():
    n = int(input())
    arr = input().strip().split(' ')

    sortedArr  = sortArray(n, arr)
    print(*sortedArr)

if __name__=="__main__":
    main()
