import functools
from collections import Counter
"""
Using comparator function we are sorting objects based on values
and then based on alphabetical order using slicing we are cutting the array
"""

def sortMap(x, y):
    # Here x and y are two key, value pairs
    if x[1] > y[1]:
        return 1
    elif x[1] < y[1]: 
        return -1
    else:
        # No swap
        if x[0].lower() < y[0].lower():
            return 1
        # Swap
        else:
            return -1

def frequentWords(words, k):
    # Base variables
    res = []
    mp = Counter(words)
    mp = sorted(mp.items(), key = functools.cmp_to_key(sortMap), reverse=True)[:k]
    
    for i in mp:
        res.append(i[0])
    return res

def main():
    n = int(input())
    words = input().strip().split()
    k = int(input())
    result = frequentWords(words ,k)
    print('\n'.join(result))

if __name__ == "__main__":
    main()