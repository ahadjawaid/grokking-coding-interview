def findStringPermutationByChangingCase(s):
    permutations = [s]

    for i in range(len(s)):
        if s[i].isalpha():
            for j in range(len(permutations)):
                newCase = list(permutations[j])
                newCase[i] = newCase[i].swapcase()
                permutations.append(''.join(newCase))

    return permutations


print(findStringPermutationByChangingCase('Ab12a'))
