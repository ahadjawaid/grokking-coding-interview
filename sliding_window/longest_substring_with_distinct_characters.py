def longestDistinctSubstring(string):
    l, maxLen = 0, 0
    charMapToIndex = {}

    for r in range(len(string)):
        if string[r] in charMapToIndex:
            l = max(l, charMapToIndex[string[r]] + 1)

        charMapToIndex[string[r]] = r

        maxLen = max(maxLen, r-l + 1)

    return maxLen


string = ["aabccbb", "abbbb", "abccde"]
for str in string:
    print(longestDistinctSubstring(str))

# 3 2 3
