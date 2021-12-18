"""
Longest substring with k distinct characters
"""

def length_of_substring(s, k):
    # base variables and dict requirement
    l, r, max_len, mp = 0, 0, 0, {}
    n = len(s)

    # Base case
    if k > n:
        return n

    # Right pointer loop
    while r < n:
        # if map size becomes more than k then we remove from left
        while len(mp) > k:
            if mp[s[l]] == 1:
                mp.pop(s[l])
            else:
                mp[s[l]] -= 1
            l += 1

        # fill map using right pointer and move towards n
        if s[r] not in mp:
            mp[s[r]] = 1
        else:
            mp[s[r]] += 1
        r += 1

        # we store max_len in this case, we use < to take care of edge cases
        if len(mp) <= k:
            max_len = max(max_len, r-l)
            # print("max: {}".format(max_len))
    return max_len

def main():
    n, k = map(int, input().split())    
    s = input()
    answer = length_of_substring(s, k)
    print(answer)

if __name__ == "__main__":
    main()