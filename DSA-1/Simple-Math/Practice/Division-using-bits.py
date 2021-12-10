"""
Dividend and divisor is given, performed division without using
multiplication, division or mod operator to determine the quotient
"""
def divideTwoIntegers(dividend, divisor):
    # This performs XOR operation and get the quotients sign
    sign = (-1 if((dividend < 0) ^
                  (divisor < 0)) else 1)

    # remove sign of operands
    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    temp = 0

    # Check each bit from right to left
    # when condition becomes true we add 2^i th bit to quotient
    for i in range(31, -1, -1):
        if (temp + (divisor << i) <= dividend):
            temp += divisor << i
            quotient |= 1 << i

    # Self explanatory code that gives the sign to the quotient
    if sign == -1:
      quotient=-quotient
    return quotient

if __name__ == '__main__':
    dividend = int(input())
    divisor = int(input())
    result = divideTwoIntegers(dividend, divisor)
    print(result)
