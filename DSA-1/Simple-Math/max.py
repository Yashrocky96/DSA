"""
This is a straight-forward self-explanatory code
simple explanation for max function in python but only for 3 numbers
"""

def findLargestNumber(a, b, c):
    Max = a
    if Max < b:
        Max = b
    elif Max < c:
        Max = c

    return Max


# NOTE: Please do not modify this function
def main():
    a, b, c = map(float, input().split(' '))
    ans = findLargestNumber(a, b, c)
    if(ans.is_integer()):
        ans = int(ans)
    print(ans)


if __name__ == "__main__":
    main()
