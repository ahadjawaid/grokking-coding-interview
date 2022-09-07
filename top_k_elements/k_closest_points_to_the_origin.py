from heapq import *
from re import X


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, comparingTo):
        return self.distanceFromOrigin() > comparingTo.distanceFromOrigin()

    def __str__(self):
        return f'[{self.x}, {self.y}]'

    def distanceFromOrigin(self):
        return (self.x ** 2) + (self.y ** 2)


def k_closest_points_to_the_origin(points, k):
    maxHeap = []

    for i in range(k):
        heappush(maxHeap, Point(*points[i]))

    for i in range(k, len(points)):
        currPoint = Point(*points[i])

        if currPoint > maxHeap[0]:
            heappop(maxHeap)
            heappush(maxHeap, currPoint)

    return list(map(lambda x: [x.x, x.y], maxHeap))


print(k_closest_points_to_the_origin([[1, 3], [2, -1], [10, 3], [1, 1]], 3))
