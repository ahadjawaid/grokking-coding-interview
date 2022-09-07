def longestSubbarryAfterReplacement(nums, k):
    maxLen, l = 0, 0
    freqOfNum = [0, 0]

    for r in range(len(nums)):
        freqOfNum[nums[r]] += 1

        if freqOfNum[0] > k:
            freqOfNum[nums[l]] -= 1
            l += 1

        maxLen = max(maxLen, r - l + 1)

    return maxLen


testCases = [[[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2],
             [[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3]]

for nums, k in testCases:
    print(longestSubbarryAfterReplacement(nums, k))

# 6
# 9
