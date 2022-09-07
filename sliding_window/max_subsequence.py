def maxSubsequence(array):
    if not array:
        return 0

    l = 0
    currSum, maxSum = 0, 0

    for r in range(len(array)):
        currSum += array[r]

        while currSum < maxSum and l <= r:
            currSum -= array[l]
            l += 1

        maxSum = max(maxSum, currSum)

    return maxSum


print(maxSubsequence([1, 3, -5, 10, 2, -10, 305, 10, 100, -2]))

# [1, 3, -5, 10, 2]
