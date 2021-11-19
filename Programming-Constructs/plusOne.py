"""
Learn array manipulation when instead we can simply
go for converting integer to and fro list
"""

def plusOne(digits):

    for i in range(len(digits)-1, -1, -1):
        # Most cases are solved first, Less checks are needed in this case
        if digits[i] != 9:
            digits[i] += 1
            break
        elif digits[i] == 9 and i == 0:
            digits[i] = 0
            digits.insert(0, 1)
        else:
            digits[i] = 0
            carry = 1
    return digits

if __name__ == '__main__':
    digits = input().split()
    digits = [int(i) for i in digits]
    result = plusOne(digits)
    for i in result:
        print(i,end=' ')
