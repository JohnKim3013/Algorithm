def solution(my_string):
    answer = ''
    a = my_string.lower()
    for i in sorted(a):
        answer += i
    return answer