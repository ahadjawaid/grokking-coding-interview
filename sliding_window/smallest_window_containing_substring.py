from cgitb import small


def smallestWindowContainingSubstring(string, pattern):
    l, matched, patternCount = 0, 0, {}
    smallestSubstring = string + 'a'

    for chr in string:
        if chr not in patternCount:
            patternCount[chr] = 0
        patternCount[chr] += 1

    for r in range(len(string)):
        if string[r] in patternCount:
            patternCount[string[r]] -= 1

            if patternCount[string[r]] >= 0:
                matched += 1

        while matched == len(patternCount):
            if string[l] in patternCount:
                patternCount[string[l]] += 1
                matched -= 1
                l += 1
            else:
                l += 1
                smallestSubstring = (smallestSubstring if len(
                    smallestSubstring) < len(string[l:r+1]) else string[l:r+1])

    return smallestSubstring


testCases = [["aabdec", "abc", "abdec"],
             ["aabdec", "abac", "aabdec"],
             ["abdbca", "abc", "abc"],
             ["adcad", "abc", "abc"]]

for string, pattern, correctAnswer in testCases:
    output = smallestWindowContainingSubstring(string, pattern)

    print(
        ("Correct Answer: {}".format(output) if output == correctAnswer else
         "Incorrect Answer: {}, Expected: {}".format(output, correctAnswer))
    )
