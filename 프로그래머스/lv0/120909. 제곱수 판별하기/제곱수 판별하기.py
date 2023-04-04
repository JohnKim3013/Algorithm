def solution(n):
    sqrt = n ** (1/2)    
    if sqrt== int(sqrt):
        answer = 1
    else:
        answer = 2
    return answer