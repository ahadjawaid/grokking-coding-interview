def findAllMissingNumbers(nums):
    currIndex, n = 0, len(nums)

    while currIndex < n:
        correctIndex = nums[currIndex] - 1
        if nums[currIndex] != nums[correctIndex]:
            nums[currIndex], nums[correctIndex] = nums[correctIndex], nums[currIndex]
        else:
            currIndex += 1

    missingNumbers = []
    for currIndex in range(n):
        if nums[currIndex] != currIndex + 1:
            missingNumbers.append(currIndex + 1)

    return missingNumbers


nums = [2, 3, 1, 8, 2, 3, 5, 1]
print(findAllMissingNumbers(nums))
