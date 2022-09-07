def permutationInString(s, pattern):
    # permutation is contiguous
    # Time: O ( N + M ) Space: O ( N + M )
    windowSize, l = len(pattern), 0
    patternCharCount, windowCharCount = {}, {}

    for char in pattern:
        if char not in patternCharCount:
            patternCharCount[char] = 0
        patternCharCount[char] += 1

    for r in range(len(s)):
        if s[r] not in windowCharCount:
            windowCharCount[s[r]] = 0
        windowCharCount[s[r]] += 1

        if len(s[l:r+1]) >= windowSize:
            if windowCharCount == patternCharCount:
                return True
            else:
                if windowCharCount[s[l]] > 1:
                    windowCharCount[s[l]] -= 1
                else:
                    del windowCharCount[s[l]]

                l += 1

    return False


testCases = [["oidbcaf", "abc"],
             ["odicf", "dc"],
             ["bcdxabcdy", "bcdyabcdx"],
             ["aaacb", "abc"]]
# True False True True

for s, pattern in testCases:
    print(permutationInString(s, pattern))
