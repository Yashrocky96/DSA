"""
Fibonacci Series without recursion using a loop
Using recursion we will have exponential time complexity
"""

def nthFibonacciNumber(n):
    a = 0
    b = 1

    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b

# NOTE: Please do not modify this function
def main():
    n = int(input())
    result = nthFibonacciNumber(n)
    print(result)

if __name__=="__main__":
    main()
