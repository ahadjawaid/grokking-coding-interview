def sqrt(n, percision):
    l, r = 0, n

    while l < r:
        mid = (r + l) / 2
        midSquared = mid * mid

        if n - percision <= midSquared <= n + percision:
            return round(mid, 2)

        elif midSquared > n:
            r = mid

        else:
            l = mid


print(sqrt(10, 0.001))
