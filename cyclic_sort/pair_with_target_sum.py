def pairWithTargetSum(nums, target):
    # Given Sorted List
    l, r = 0, len(nums) - 1

    while l < r:
        currSum = nums[l] + nums[r]

        if currSum == target:
            return [l, r]

        elif currSum > target:
            r -= 1

        elif currSum < target:
            l += 1


array, target = sorted([1, 35, 6, 7, 2, 1]), 9
print(array)
print(pairWithTargetSum(array, target))
