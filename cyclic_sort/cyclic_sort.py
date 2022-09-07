def cyclicSort(array):
    # For array with ints that ranges from (1 to n)

    for i in range(len(array)):
        if i != array[i]:
            array[array[i] - 1], array[i] = array[i], array[array[i] - 1]


array = [3, 5, 1, 2, 4, 6, 7]
cyclicSort(array)
print(array)
