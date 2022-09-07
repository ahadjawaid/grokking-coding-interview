def diffrent_ways_to_evaluate_expression(expression):
    result = []

    if '+' not in expression and '-' not in expression and '*' not in expression:
        result.append(int(expression))
    else:
        for i in range(len(expression)):
            elem = expression[i]

            if not elem.isdigit():
                leftSide = diffrent_ways_to_evaluate_expression(expression[:i])
                rightSide = diffrent_ways_to_evaluate_expression(
                    expression[i+1:])

                for firstPart in leftSide:
                    for secondPart in rightSide:
                        if elem == '*':
                            result.append(firstPart * secondPart)
                        elif elem == '+':
                            result.append(firstPart + secondPart)
                        elif elem == '-':
                            result.append(firstPart - secondPart)

    return result


print(diffrent_ways_to_evaluate_expression('1+1*3'))
