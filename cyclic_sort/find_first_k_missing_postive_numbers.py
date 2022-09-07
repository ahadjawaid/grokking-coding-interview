def findFirstKMissingPostiveNumbers(nums, k):
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if 0 <= nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    i = 0
    missing = []
    while len(missing) != k:
        if i < n and nums[i] != i + 1:
            missing.append(i + 1)
        elif i >= n:
            missing.append(i + 1)
        i += 1

    return missing


nums, k = [3, -1, 4, 5, 5], 5
nums2, k2 = [2, 3, 4], 3
print(findFirstKMissingPostiveNumbers(nums2, k2))
