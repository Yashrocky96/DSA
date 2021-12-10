"""
Input has been handled by the problem maker
This executes the behavior of queue that is FIFO
"""

from collections import deque

class Solution:

    def __init__(self):
        self.queue = deque()
    def insert(self, num):
        self.queue.append(num)

    def getFirst(self):
        return self.queue.popleft()
