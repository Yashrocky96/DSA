"""
Performs modulo of a number using recursion this is a heavy operation
Not good to use this program to find modulo
"""

def moduloUsingRecursion(a, b):
    if b==0:  # Divisor 
        return -1
    elif a < b:
        return abs(a)
    else:
        return moduloUsingRecursion(a-b, b)

def main():
    a, b = map(int, input().split())
    result = moduloUsingRecursion(a, b)
    print(result)

if __name__ == '__main__':
    main()
