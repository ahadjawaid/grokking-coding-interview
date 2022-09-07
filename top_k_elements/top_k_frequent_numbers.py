from collections import Counter
from heapq import *


def top_k_frequent_numbers(arr, k):
    frequency = Counter(arr)
    minHeap = []

    for num, freq in frequency.items():
        heappush(minHeap, (freq, num))

        if len(minHeap) > k:
            heappop(minHeap)

    return list(map(lambda x: x[1], minHeap))


print("Here are the K frequent numbers: " +
      str(top_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

print("Here are the K frequent numbers: " +
      str(top_k_frequent_numbers([5, 12, 11, 3, 11], 2)))
