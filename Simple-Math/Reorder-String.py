"""
For given string and the place of it's letters as space separated
input

We reorder the string
"""

def stringPermutation(n, s, per):
    s = list(s)
    result = [None for i in range(n)]
    for i in range(n):
        result[per[i] - 1] = s[i]

    return "".join(result)

# NOTE: Please do not modify this function
def main():
    n = int(input())
    s = input()
    per = list(map(int, input().strip().split(' ')))

    result = stringPermutation(n, s, per)
    print(result)

if __name__=="__main__":
    main()
