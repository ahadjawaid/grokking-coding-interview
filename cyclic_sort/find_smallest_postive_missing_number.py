def findSmallestPostiveMissingNumber(nums):
    i, n = 0, len(nums)

    for i in range(n):
        j = nums[i] - 1
        if 0 <= nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1


nums = [-3, 1, 5, 4, 2]
nums2 = [3, -2, 0, 1, 2]
print(findSmallestPostiveMissingNumber(nums2))
