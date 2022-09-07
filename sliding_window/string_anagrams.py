def stringAnagrams(s, pattern):
    l, patternCharCount, stringCharCount = 0, {}, {}
    firstIndexForMatch = []

    for char in pattern:
        if char not in patternCharCount:
            patternCharCount[char] = 0
        patternCharCount[char] += 1

    for r in range(len(s)):
        if s[r] not in stringCharCount:
            stringCharCount[s[r]] = 0
        stringCharCount[s[r]] += 1

        if len(s[l:r+1]) > len(pattern):
            if stringCharCount[s[l]] > 1:
                stringCharCount[s[l]] -= 1
            else:
                del stringCharCount[s[l]]

            l += 1

        if stringCharCount == patternCharCount:
            firstIndexForMatch.append(l)

    return firstIndexForMatch


testCases = [["ppqp", "pq"],
             ["abbcabc", "abc"]]
# True False True True

for s, pattern in testCases:
    print(stringAnagrams(s, pattern))
