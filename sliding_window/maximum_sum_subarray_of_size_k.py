from curses import window


def maxSumSubarrayK(nums, k):
    windowSum, maxSum, l = 0, 0, 0

    for r in range(len(nums)):
        windowSum += nums[r]
        if r >= k - 1:
            maxSum = max(maxSum, windowSum)
            windowSum -= nums[l]
            l += 1

    return maxSum


nums, k = [2, 1, 5, 1, 3, 2], 3

print(maxSumSubarrayK(nums, k))
