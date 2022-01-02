# Diamond design printing given for a number
def patternPrintingII(n):
    arr = []
    for i in range(n):
        arr.append((n-i)*" " + "* " + i* "* ")
    for i in range(n-2, -1, -1):
        arr.append((n-i)*" " + "* " + i* "* ")
    return arr

# NOTE: Please do not modify this function
def main():
    n = int(input())

    pattern = patternPrintingI(n)

    for i in pattern:
        print(i)


if __name__ == "__main__":
    main()
