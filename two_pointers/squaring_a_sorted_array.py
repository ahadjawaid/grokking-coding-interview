def squaring_a_sorted_array(array):
    result = [0 for _ in range(len(array))]
    l, r = 0, len(array) - 1
    currIndex = len(array) - 1

    while l <= r:
        rightSquared = array[r] ** 2
        leftSquared = array[l] ** 2

        if rightSquared >= leftSquared:
            result[currIndex] = rightSquared
            r -= 1
        else:
            result[currIndex] = leftSquared
            l += 1

        currIndex -= 1

    return result


print("Squares: " + str(squaring_a_sorted_array([-2, -1, 0, 2, 3])))
print("Squares: " + str(squaring_a_sorted_array([-3, -1, 0, 1, 2])))
