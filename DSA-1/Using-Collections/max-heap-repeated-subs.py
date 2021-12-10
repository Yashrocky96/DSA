"""
Using priority queue we define the max heap by multiply * -1
This gets 2 max elements push it's abs diff into the array
"""

from queue import PriorityQueue
def reduceArray(n, arr):
    # For max heap multiply each value with -1
    heap = PriorityQueue()
    for i in arr:
        heap.put(-1 * i)
    while (heap.qsize() > 1):
        # Remove largest element
        X = -1 * heap.get()
        # Remove 2nd largest element
        Y = -1 * heap.get()

        # If extracted elements
        # are not equal
        if (X != Y):
            # Find X - Y and push
            # it to heap
            diff = abs(X - Y)
            heap.put(-1 * diff)

    # If heap size is 1, then
    # print the remaining element
    if (heap.qsize() == 1):
        return -1 * heap.get()
    else:
        return 0

# NOTE: Please do not modify this function
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    res = reduceArray(n, arr)
    print(res)


if __name__ == "__main__":
    main()
