from collections import deque


def permutation(arr):
    result = []
    n = len(arr)

    permutations = deque([[]])

    for num in arr:
        for _ in range(len(permutations)):
            currSet = permutations.popleft()

            for i in range(len(currSet) + 1):
                newSet = list(currSet)
                newSet.insert(i, num)

                if len(newSet) == n:
                    result.append(newSet)
                else:
                    permutations.append(newSet)

    return result


print("Here are all the permutations: " + str(permutation([1, 3, 5])))
