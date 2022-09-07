from heapq import *


def find_sum_of_elements(arr, k1, k2):
    minHeap = []

    for num in arr:
        heappush(minHeap, num)

    sumBetweenK1AndK2 = 0

    for _ in range(k1):
        heappop(minHeap)

    for _ in range(k2 - k1 - 1):
        sumBetweenK1AndK2 += heappop(minHeap)

    return sumBetweenK1AndK2


print("Sum of all numbers between k1 and k2 smallest numbers: " +
      str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
print("Sum of all numbers between k1 and k2 smallest numbers: " +
      str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))
