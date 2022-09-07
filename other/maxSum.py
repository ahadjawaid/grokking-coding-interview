# Divide and conquer maxSubbarray

def maxSubbarray(arr, left, right):
    if left == right:
        return arr[0]

    center = (left + right) / 2
    maxLeftSum = maxSubbarray(arr, left, center)
    maxRightSum = maxSubbarray(arr, center + 1, right)

    maxLeftBorderSum, leftBorderSum = 0, 0
    for i in range(left, len(arr), -1):
        leftBorderSum += arr[i]
        maxLeftBorderSum = max(leftBorderSum, maxLeftBorderSum)

    maxRightBorderSum, rightBorderSum = 0, 0
    for i in range(0, right, 1):
        rightBorderSum += arr[i]
        maxLeftBorderSum = max(rightBorderSum, maxLeftBorderSum)

    return max(maxLeftSum, maxRightSum, maxLeftBorderSum+maxRightBorderSum)


arr = [1, 2, -4, 3, -1]

print(maxSubbarray(arr, 0, len(arr) - 1))
