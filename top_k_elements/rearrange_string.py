from heapq import *
from collections import Counter


def rearrange_string(s):
    frequencyOfChars = Counter(s)

    maxHeap = []
    for char, freq in frequencyOfChars.items():
        heappush(maxHeap, (-freq, char))

    newString = []
    prevChar, prevFreq = '', 0
    while maxHeap:
        freq, char = heappop(maxHeap)

        if prevChar and -prevFreq > 0:
            heappush(maxHeap, (prevFreq, prevChar))

        newString.append(char)
        prevFreq, prevChar = freq + 1, char

    return ''.join(newString) if len(newString) == len(s) else ''


print("Rearranged string:  " + rearrange_string("aappp"))
print("Rearranged string:  " + rearrange_string("Programming"))
print("Rearranged string:  " + rearrange_string("aapa"))
