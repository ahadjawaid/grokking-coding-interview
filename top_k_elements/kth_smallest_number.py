from heapq import *


def kth_smallest_number(array, k):
    maxHeap = []

    for i in range(k):
        heappush(maxHeap, -array[i])

    for i in range(k, len(array)):
        if maxHeap[0] < -array[i]:
            heappop(maxHeap)
            heappush(maxHeap, -array[i])

    return -maxHeap[0]


print("Kth smallest number is: " +
      str(kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

print("Kth smallest number is: " +
      str(kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

print("Kth smallest number is: " +
      str(kth_smallest_number([5, 12, 11, -1, 12], 3)))
