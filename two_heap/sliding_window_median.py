import heapq


class slidingWindowMedian:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def insertNum(self, num):
        # Want to get the middle elements as top element in min and max heap
        if not self.maxHeap or self.maxHeap[0] >= num:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        self.reblanceHeaps()

    def reblanceHeaps(self):
        minLen = len(self.minHeap)
        maxLen = len(self.maxHeap)

        if maxLen > minLen + 1:
            heapq.heappush(self.minHeap, heapq.heappop(self.maxHeap))
        elif maxLen == minLen:
            heapq.heappush(self.maxHeap, heapq.heappop(self.minHeap))

    def removeItem

    def slidingWindowMean(array, k):
