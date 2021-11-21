"""
Convert decimals to given base number
limit: [0-9][A-F]
"""

def decimalToBaseConversion(num, base):
    res = []

    if base > 9:
        while num > 0:
            rem = num%base
            if rem > 9:
                if rem == 10:
                    rem = 'A'
                elif rem == 11:
                    rem = 'B'
                elif rem == 12:
                    rem = 'C'
                elif rem == 13:
                    rem = 'D'
                elif rem == 14:
                    rem = 'E'
                elif rem == 15:
                    rem = 'F'
            res.insert(0, str(rem))
            num //= base

    else:
        while num > 0:
            res.insert(0, str(num%base))
            num //= base

    return "".join(res)

# NOTE: Please do not modify this function
def main():
    num, base = map(int, input().split(' '))
    ans = decimalToBaseConversion(num, base)
    print(ans)


if __name__ == "__main__":
    main()
