"""
Using array or list to store the digits of large numbers
To solve the limitations of holder data types such as int, long etc
Python handles them better, but using this solution is good
due to factorial numbers being huge.
"""

def multiply(arr, val):
    """
    This function calculates n * prev!
    (or any given value in the form of array of integers)
    """
    carry = 0
    mul = 0
    for i in range(len(arr)):
        mul = (arr[i] * val) + carry
        carry = mul // 10
        arr[i] = mul % 10
    if carry > 0:
        arr.append(carry)

def largeFactorial(num):
    result = [1]
    for i in range(2, num+1):
        multiply(result, i)

    result.reverse()
    result = int(''.join(map(str, result)))
    return result

# NOTE: Please do not modify this function
def main():
    num = int(input())
    factorial = largeFactorial(num)
    print(factorial)

if __name__=="__main__":
    main()
