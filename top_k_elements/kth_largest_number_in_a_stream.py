from heapq import *


class KthLargestNumberInStream:
    def __init__(self, array, k):
        self.minHeap = []
        self.k = k

        for num in array:
            self.add(num)

    def add(self, value):
        heappush(self.minHeap, value)

        if len(self.minHeap) > self.k:
            heappop(self.minHeap)

        return self.minHeap[0]


kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
print("4th largest number is: " + str(kthLargestNumber.add(6)))
print("4th largest number is: " + str(kthLargestNumber.add(13)))
print("4th largest number is: " + str(kthLargestNumber.add(4)))
