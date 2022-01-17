"""
"""
# Initializes two lists, this isn't proper stacks, but implementation is similar
stack = []
minStack = []

def push(x):
    stack.append(x)
    # minStack is not empty
    if minStack:
        # comparing before inserting new element, here x is smaller
        if x < minStack[-1]:
            minStack.append(x)
        # Only storing minimum value or duplicating top in case x is greater
        else:
            minStack.append(minStack[-1])
    else:
        minStack.append(x)

# Matches both stacks and pops them both
def pop():
    if stack and minStack:
        stack.pop()
        minStack.pop()

# Top value of minStack returns the minimum value in the stack
def findMin():
    if minStack:
        return minStack[-1]
    else:
        return -1

queries = int(input())

for query in range(queries):
    _type = input().strip().split()
    x = 0
    if len(_type) == 2:
        _type, x = map(int, _type)
    else:
        _type = int(_type[0])
    if _type == 1:
        push(x)
    elif _type == 2:
        pop()
    else:
        minElement = findMin()
        print(minElement)