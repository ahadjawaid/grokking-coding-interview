from heapq import *


def connect_ropes(arr):
    minHeap = []
    totalCost = 0
    currCost = 0

    for num in arr:
        heappush(minHeap, num)

    while len(minHeap) > 1:
        firstRope, secondRope = heappop(minHeap), heappop(minHeap)

        currCost = firstRope + secondRope
        totalCost += currCost

        heappush(minHeap, currCost)

    return totalCost


print("Minimum cost to connect ropes: " +
      str(connect_ropes([1, 3, 11, 5])))
print("Minimum cost to connect ropes: " +
      str(connect_ropes([3, 4, 5, 6])))
print("Minimum cost to connect ropes: " +
      str(connect_ropes([1, 3, 11, 5, 2])))
