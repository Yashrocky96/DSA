"""
This adds two strings that are represented as integers and returns a string
"""

def bigIntegerAddition(s1, s2):
    s1 = s1[::-1]
    s2 = s2[::-1]

    if len(s1) < len(s2):
        s1, s2 = s2, s1

    carry = 0
    result = []
    for i in range(len(s2)):
        add = int(s1[i]) + int(s2[i]) + carry
        carry = 0
        if add > 9:
            carry = add // 10
            add = add % 10
        result.append(str(add))

    for i in range(len(s2), len(s1)):
        add = int(s1[i]) + carry
        carry = 0
        if add > 9:
            carry = add // 10
            add = add % 10
        result.append(str(add))

    if carry > 0:
        result.append(str(carry))


    result = "".join(result)[::-1]
    return result

# NOTE: Please do not modify this function
def main():
    s1, s2 = input().split(' ')
    add = bigIntegerAddition(s1, s2)
    print(add)


if __name__ == "__main__":
    main()
