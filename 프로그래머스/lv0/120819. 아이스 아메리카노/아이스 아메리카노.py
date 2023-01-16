def solution(money):
    answer = []
    answer.insert(0, money // 5500)
    answer.insert(1, money % 5500)
    return answer