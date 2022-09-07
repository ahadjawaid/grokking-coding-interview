def fruitsInBasket(fruits):
    # Maxlen Subarray with at most 2 distinct elements
    l, maxFruits = 0, 0
    currentFruits = {}

    for r in range(len(fruits)):
        if fruits[r] not in currentFruits:
            currentFruits[fruits[r]] = 0
        currentFruits[fruits[r]] += 1

        while len(currentFruits) > 2:
            currentFruits[fruits[l]] -= 1
            if currentFruits[fruits[l]] == 0:
                del currentFruits[fruits[l]]

            l += 1

        maxFruits = max(maxFruits, r-l + 1)

    return maxFruits


fruit = ['A', 'B', 'C', 'A', 'C']
fruit2 = ['A', 'B', 'C', 'B', 'B', 'C']
print(fruitsInBasket(fruit))  # -> 3
print(fruitsInBasket(fruit2))  # -> 5
