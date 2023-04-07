def solution(array):
    a = ""
    answer = 0
    for i in array:
        a+=str(i)
    for j in a:
        if int(j) == 7:
            answer+=1        
    return answer