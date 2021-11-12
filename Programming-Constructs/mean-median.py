import math
"""
Calculating statistics of an array upto 5 decimals accuracy

Note: We can also use sum() to get the sum of the array
"""
def mean(n, a):
    """
    sum all values in the array and then divide by the length
    that is n number of elements to get the mean
    """
    avg = 0
    for i in a:
        avg += i
    avg /= n
    return round(avg, 5)

def median(n, a):
    """
    """
    a.sort()
    print(a)
    if n % 2 == 0:
        return (a[int((n/2)-1)]+a[int(n/2)])/2
    else:
        return a[math.ceil(n/2)]

# NOTE: Please do not modify this function
def main():
    n=int(input())
    a=list(map(float,input().split()))
    m1, m2 = mean(n,a), median(n,a)
    print("Mean: {}\nMedian: {}".format(m1, m2))

if __name__=="__main__":
    main()
