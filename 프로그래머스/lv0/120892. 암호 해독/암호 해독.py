def solution(cipher, code):
    answer = ''
    for i in range(len(cipher)//code):
        print(i)
        answer = answer + cipher[code*(i+1)-1]
    return answer