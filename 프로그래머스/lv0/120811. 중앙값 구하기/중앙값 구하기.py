def solution(array):
    array.sort()
    l = len(array)
    if l % 2 != 0:
        
        answer = array[(l//2)]
        
    else:
        
        answer = (array[(l//2)-1] + array[(l//2)])/2
    
    return answer