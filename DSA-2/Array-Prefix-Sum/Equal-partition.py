"""
Find equal partitions where left and right sum becomes equal from a given index
Use prefix and suffix to solve these problems
"""

def equalPartition(n, arr):
    prefix, suffix = [], []
    temp = 0
    for i in range(n):
        temp += arr[i]
        prefix.append(temp)
    temp = 0
    for j in range(n-1, -1, -1):
        temp += arr[j]
        suffix.append(temp)
    suffix = suffix[::-1]

    for i in range(n):
        if prefix[i] == suffix[i]:
            return i
    return -1

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = equalPartition(n, arr)
    print(result)

if __name__=="__main__":
    main()
