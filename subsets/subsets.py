from hashlib import new


def subsets(array):
    subsets = [[]]

    n = len(array)
    for num in array:
        for i in range(len(subsets)):
            newSet = [*subsets[i], num]
            subsets.append(newSet)

    return subsets


print(subsets([1, 2, 3]))
