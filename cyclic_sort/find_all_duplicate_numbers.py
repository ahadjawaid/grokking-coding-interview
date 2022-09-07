def findDuplicateNumbers(nums):
    currIndex, n = 0, len(nums)
    duplicates = []

    while currIndex < n:
        correctIndex = nums[currIndex] - 1
        if nums[currIndex] != nums[correctIndex]:
            nums[currIndex], nums[correctIndex] = nums[correctIndex], nums[currIndex]
        else:
            currIndex += 1

    for i in range(n):
        if nums[i] != i + 1:
            duplicates.append(nums[i])

    return duplicates


nums = [3, 4, 4, 5, 5]
print(findDuplicateNumbers(nums))
