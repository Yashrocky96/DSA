"""
Insert elements function defined
getMax() will pop and remove from array and give you the max number
"""

from heapq import heappop, heappush, heapify

# Creating empty heap
heap = []
heapify(heap)

def insert(num):
    heappush(heap, -1 * num)

def getMax():
    return (-1 * heappop(heap))

"""
Define main function to use this py file
"""
