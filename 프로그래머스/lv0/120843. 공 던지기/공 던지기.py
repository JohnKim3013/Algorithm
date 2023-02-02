def solution(numbers, k):
    repeat_numbers = numbers * k 
    answer = repeat_numbers[2*(k-1)]
    return answer