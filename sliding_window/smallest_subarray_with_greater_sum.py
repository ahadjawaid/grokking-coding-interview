from math import inf


def smallestSubarrayWithGreaterSum(nums, s):
    windowSum, smallestLen = 0, inf
    l = 0

    for r in range(len(nums)):
        windowSum += nums[r]

        while windowSum >= s:
            smallestLen = min((r - l) + 1, smallestLen)
            windowSum -= nums[l]
            l += 1

    return 0 if smallestLen == inf else smallestLen


nums, s = [2, 1, 5, 2, 3, 2], 7
nums2, s2 = [2, 1, 5, 2, 8], 7
nums3, s3 = [3, 4, 1, 1, 6], 8

print(smallestSubarrayWithGreaterSum(nums3, s3))
