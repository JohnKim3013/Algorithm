def solution(my_string):
    answer = []
    sorted_string=''.join(sorted(my_string))
    print(sorted_string)
    for i in sorted_string:
        if i in '0123456789':
            answer.append(int(i))
    return answer