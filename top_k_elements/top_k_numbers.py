import heapq


def top_k_numbers(array, k):
    minHeap = []

    for i in range(k):
        heapq.heappush(minHeap, array[i])

    for i in range(k, len(array)):
        if minHeap[0] < array[i]:
            heapq.heappop(minHeap)
            heapq.heappush(minHeap, array[i])

    return minHeap


print("Here are the top K numbers: " +
      str(top_k_numbers([3, 1, 5, 12, 2, 11], 3)))

print("Here are the top K numbers: " +
      str(top_k_numbers([5, 12, 11, -1, 12], 3)))
