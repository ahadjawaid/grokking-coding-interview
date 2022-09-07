def findMissingNumber(nums):
    currIndex, n = 0, len(nums)

    while currIndex < n:
        correctIndex = nums[currIndex]
        if nums[currIndex] < n and nums[currIndex] != nums[correctIndex]:
            nums[currIndex], nums[correctIndex] = nums[correctIndex], nums[currIndex]
        else:
            currIndex += 1

    for currIndex in range(0, n):
        if nums[currIndex] != currIndex:
            return currIndex


nums = [4, 0, 3, 1]
print(findMissingNumber(nums))
