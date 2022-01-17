"""
Using stack LIFO to find the next greater element
"""

def nextLargerElement(arr):
    # Initializing base variables
    s, res = [], [-1]

    #  Push top/end element of array to stack
    s.append(arr[-1])
    
    for i in range(len(arr)-2, -1, -1):
        '''
        if stack not empty and if stack top is less than array value pop till we find next greater element
        '''
        while s and arr[i] >= s[-1]:
            s.pop()
        
        # stack is empty no NGE so -1 else stacks top value
        if not s:
            res.append(-1)
        else:
            res.append(s[-1])

        # loop adding all values of array to stack
        s.append(arr[i])
        
    # reversing array or use insert instead of append
    return res[::-1]

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().strip().split()))
    result = nextLargerElement(arr)
    print(*result)