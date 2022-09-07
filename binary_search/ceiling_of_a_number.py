def ceiling_of_a_number(arr, target):
    l, r = 0, len(arr) - 1

    if target > arr[r]:
        return -1

    while l <= r:
        mid = l + (r - l) // 2
        midValue = arr[mid]

        if midValue == target:
            return mid

        elif midValue < target:
            l = mid + 1
        else:
            r = mid - 1

    return l


print(ceiling_of_a_number([4, 6, 10], 6))
print(ceiling_of_a_number([1, 3, 8, 10, 15], 12))
print(ceiling_of_a_number([4, 6, 10], 17))
print(ceiling_of_a_number([4, 6, 10], -1))
