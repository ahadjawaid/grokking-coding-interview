def subsetWithDuplicates(array):
    distinctSubsets = [[]]
    visited = set()

    for num in array:
        for i in range(len(distinctSubsets)):
            newSet = list(distinctSubsets[i])
            newSet.append(num)

            if tuple(newSet) not in visited:
                distinctSubsets.append(newSet)
                visited.add(tuple(newSet))

    return distinctSubsets


print("Here is the list of subsets: " + str(subsetWithDuplicates([1, 3, 3])))
print("Here is the list of subsets: " +
      str(subsetWithDuplicates([1, 5, 3, 3])))
