from collections import Counter, deque
from heapq import *


def rearrange_string_k_distance_apart(s, k):
    maxHeap = []
    frequencyOfChars = Counter(s)

    for char, freq in frequencyOfChars.items():
        heappush(maxHeap, (-freq, char))

    queue = deque([])
    newString = []
    while maxHeap:
        freq, char = heappop(maxHeap)

        newString.append(char)
        queue.append((freq + 1, char))

        if len(queue) == k:
            freq, char = queue.popleft()

            if -freq > 0:
                heappush(maxHeap, (freq, char))

    return ''.join(newString) if len(newString) == len(s) else ''


print("Reorganized string: " + rearrange_string_k_distance_apart("Programming", 3))
print("Reorganized string: " + rearrange_string_k_distance_apart("mmpp", 2))
print("Reorganized string: " + rearrange_string_k_distance_apart("aab", 2))
print("Reorganized string: " + rearrange_string_k_distance_apart("aapa", 3))
