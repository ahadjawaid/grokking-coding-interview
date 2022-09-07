def findDuplicateNumbers(nums):
    currIndex, n = 0, len(nums)

    while currIndex < n:
        if nums[currIndex] != currIndex + 1:
            correctIndex = nums[currIndex] - 1
            if nums[currIndex] != nums[correctIndex]:
                nums[currIndex], nums[correctIndex] = nums[correctIndex], nums[currIndex]
            else:
                return nums[currIndex]
        else:
            currIndex += 1


nums = [1, 4, 4, 3, 2]
print(findDuplicateNumbers(nums))
