from collections import Counter
from heapq import *


def maximum_distinct_elements(array, k):
    distinctCount = 0
    frequencyOfArray = Counter(array)
    minHeap = []

    for num, freq in frequencyOfArray.items():
        if freq == 1:
            distinctCount += 1
        else:
            heappush(minHeap, (freq, num))

    while minHeap and k > 0:
        freq, num = heappop(minHeap)

        if freq > 1:
            heappush(minHeap, (freq - 1, num))
            k -= 1
        else:
            distinctCount += 1

    return distinctCount - k


print("Maximum distinct numbers after removing K numbers: " +
      str(maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
print("Maximum distinct numbers after removing K numbers: " +
      str(maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
print("Maximum distinct numbers after removing K numbers: " +
      str(maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))
