from heapq import *


def k_closest_numbers(arr, k, x):
    maxHeap = []

    for i in range(len(arr)):
        distanceFromX = abs(x - arr[i])
        heappush(maxHeap, (-distanceFromX, arr[i]))

        if len(maxHeap) > k:
            heappop(maxHeap)

    return list(map(lambda x: x[1], maxHeap))


print("'K' closest numbers to 'X' are: " +
      str(k_closest_numbers([5, 6, 7, 8, 9], 3, 7)))
print("'K' closest numbers to 'X' are: " +
      str(k_closest_numbers([2, 4, 5, 6, 9], 3, 6)))
print("'K' closest numbers to 'X' are: " +
      str(k_closest_numbers([2, 4, 5, 6, 9], 3, 10)))
