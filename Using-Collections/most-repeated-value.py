"""
Gets the most mostRepeatedTemperature using dictionary in python
Time complexity becomes O(n log n)
"""

def mostRepeatedTemperature(n, temperature):
    freq = {}
    for i in temperature:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1

    max_temp = 0
    max_freq = 0
    for i in freq:
        if freq[i] > max_freq:
            max_temp = i
            max_freq = freq[i]
        elif freq[i] == max_freq:
            if i > max_temp:
                max_temp = i
    return max_temp

# NOTE: Please do not modify this function
def main():
    n = int(input())
    temperature = list(map(int, input().split()))
    res = mostRepeatedTemperature(n, temperature)
    print(res)


if __name__ == "__main__":
    main()
