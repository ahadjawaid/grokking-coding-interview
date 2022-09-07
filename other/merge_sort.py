def mergeSort(array):
    if len(array) == 1:
        return array

    midpoint = len(array) // 2

    return merge(mergeSort(array[:midpoint]), mergeSort(array[midpoint:]))


def merge(left, right):
    merged = []
    while left and right:
        merged.append(left.pop(0) if left[0] < right[0] else right.pop(0))

    merged.extend(left if left else right)

    return merged


array = [3, 56, 1, -2, 40, 342, -102]

print(mergeSort(array))
