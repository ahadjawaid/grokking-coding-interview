def longestSubstringWithKDistincy(string, k):
    l, maxLen = 0, 0
    subStringChars = {}

    for r in range(len(string)):
        if string[r] not in subStringChars:
            subStringChars[string[r]] = 0
        subStringChars[string[r]] += 1

        if r >= k - 1:
            while len(subStringChars) > k:
                if subStringChars[string[l]] > 1:
                    subStringChars[string[l]] -= 1
                else:
                    subStringChars.pop(string[l])

                l += 1

            maxLen = max(r - l + 1, maxLen)

    return maxLen


string, k = "araaci", 2
string2, k2 = "araaci", 1
string3, k3 = "cbbebi", 3
print(longestSubstringWithKDistincy(string, k))  # -> 4
print(longestSubstringWithKDistincy(string2, k2))  # -> 2
print(longestSubstringWithKDistincy(string3, k3))  # -> 5
