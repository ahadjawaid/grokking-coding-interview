from collections import Counter
from heapq import *


def frequency_sort(s):
    maxHeap = []
    letterFrequency = Counter(s)
    frequencySortedString = []

    for letter, freq in letterFrequency.items():
        heappush(maxHeap, (-freq, letter))

    while maxHeap:
        freq, letter = heappop(maxHeap)

        for _ in range(-freq):
            frequencySortedString.append(letter)

    return ''.join(frequencySortedString)


print("String after sorting characters by frequency: " +
      frequency_sort("Programming"))
print("String after sorting characters by frequency: " +
      frequency_sort("abcbab"))
