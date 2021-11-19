"""
Fizz if multiple of 3 Buzz if 5 and FizzBuzz if multiple of both
For a given integer
"""

def fizzBuzz(n):
    result = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result



def main():
    n = int(input())
    result = fizzBuzz(n)
    print('\n'.join([i for i in result]))

if __name__ == "__main__":
    main()
