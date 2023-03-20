def solution(array):
    sorted_array = sorted(array)
    max_value = sorted_array[-1]
    max_index = array.index(max_value)
    answer = [max_value, max_index]
    return answer