"""
Sum of Inifinite Geometric Progression is calculated
A/(1-R)
"""

def seriesSumII(A, R):
    return round(A/(1-R), 5)

# NOTE: Please do not modify this function
def main():

    [A, R] = list(map(float, input().split()))

    result = seriesSumII(A, R)

    print(result)


if __name__ == "__main__":
    main()
