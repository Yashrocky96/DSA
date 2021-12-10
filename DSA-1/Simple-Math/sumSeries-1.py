"""
summation of a given series, get the pattern and solve the equation
"""
def seriesSumI(n):
    sum = 0
    for i in range(1, n+1):
        sum += ((2 * i) - 1) * ((2*i) + 1)
    return sum

# NOTE: Please do not modify this function
def main():
    n = int(input())

    ans = seriesSumI(n)

    print(ans)


if __name__ == "__main__":
    main()
