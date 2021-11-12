def patternPrintingI(n):
    arr = [((n-i) * " ") + (i * "*") + "*" + (i * "*") + ((n-i) * " ") for i in range(0, n)]
    return arr


# NOTE: Please do not modify this function
def main():
    n = int(input())

    pattern = patternPrintingI(n)

    for i in pattern:
        print(i)


if __name__ == "__main__":
    main()
