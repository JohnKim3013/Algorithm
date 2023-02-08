def solution(n):
    factorial = []
    result = 1
    for i in range (1,11):
        result *= i
        factorial.append(result)
    print(factorial)
    for j in factorial:
        if n == j:
            return factorial.index(j)+1
        elif n < j:
            return factorial.index(j)