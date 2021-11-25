"""
Counts the occurences of 2s in all digits to a given number n
"""

def countOfTwos(n):
    s = ""
    for i in range(n+1):
        s += str(i)
    return s.count("2")
def main():
    n=int(input())
    result = countOfTwos(n)
    print(result)

if __name__ == "__main__":
    main()
