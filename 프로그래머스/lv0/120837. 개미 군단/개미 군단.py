def solution(hp):
    s1 = hp//5
    r1 = hp%5
    s2 = r1//3
    r2 = r1%3

    answer = s1+s2+r2
    return answer