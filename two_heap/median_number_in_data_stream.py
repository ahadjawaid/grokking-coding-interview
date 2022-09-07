from heapq import *


class MedianOfStream:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def insertNum(self, num):
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self):
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + (-self.maxHeap[0])) / 2

        return -self.maxHeap[0] / 1.0


medianOfAStream = MedianOfStream()
medianOfAStream.insertNum(3)
medianOfAStream.insertNum(1)
print("The median is: " + str(medianOfAStream.findMedian()))
medianOfAStream.insertNum(5)
print("The median is: " + str(medianOfAStream.findMedian()))
medianOfAStream.insertNum(4)
print("The median is: " + str(medianOfAStream.findMedian()))
