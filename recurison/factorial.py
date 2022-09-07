def factorial(n):
    if n < 1:
        return 1

    return n * factorial(n-1)


n = 3
print(f'Factorial of {n} is', factorial(n))


def sumArray(arr):
    if len(arr) == 0:
        return 0

    return arr[0] + sumArray(arr[1:])


array = [1, 2, 3, 4]
print(f'Sum Array of {array} is', sumArray(array))


def stringReversal(s):
    if len(s) == 0:
        return ''

    lastIndex = len(s) - 1

    return s[lastIndex] + stringReversal(s[:lastIndex])


s = 'my name is bob'
print(f'Reversed string of "{s}" is "{stringReversal(s)}"')


def countXInString(s):
    if len(s) == 0:
        return 0

    return (1 if s[0] == 'x' else 0) + countXInString(s[1:])


s = 'axbcxd'
print(f'There are {countXInString(s)} x in the string "{s}"')


def countStaircaseSteps(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1

    return countStaircaseSteps(n-1) + countStaircaseSteps(n-2) + countStaircaseSteps(n-3)


n = 3
print(f'There are {countStaircaseSteps(n)} ways to go up {n} steps')
