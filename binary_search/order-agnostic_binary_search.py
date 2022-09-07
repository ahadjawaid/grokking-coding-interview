def binary_search(arr, target):
    if not arr:
        return -1

    isReversed = arr[0] > arr[-1]

    l, r = 0, len(arr)

    while l <= r:
        mid = (r + l) // 2
        midValue = arr[mid]

        if midValue == target:
            return mid

        if isReversed:
            if midValue < target:
                r = mid - 1
            else:
                l = mid + 1

        else:
            if midValue > target:
                r = mid - 1
            else:
                l = mid + 1

    return -1


print(binary_search([4, 6, 10], 10))
print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
print(binary_search([10, 6, 4], 10))
print(binary_search([10, 6, 4], 4))
