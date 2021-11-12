# Reversing a given number
def reverseNum(num):
    rev = 0
    while num > 0:
        """
        rev*10 adds last digit to digit places
        num%10 gets the last digit

        loop the number and divide by 10 to get last digits

        """
        rev = num%10 + rev*10
        num = int(num/10)
    return rev

# NOTE: Please do not modify this function
def main():
    num = int(input())
    reversedNum = reverseNum(num)
    print(reversedNum)


if __name__ == "__main__":
    main()
