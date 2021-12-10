"""
Maximum profit calculated by always buying at low and selling at high
"""

def maxProfit(prices):
    max_profit = 0
    for i in range(1, n):
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i-1]
            
    return max_profit

if __name__ == '__main__':
    n = int(input())
    prices = input().split()
    prices = [int(i) for i in prices]
    result = maxProfit(prices)
    print(result)