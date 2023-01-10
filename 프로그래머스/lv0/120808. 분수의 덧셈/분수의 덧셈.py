import math

def solution(numer1, denom1, numer2, denom2):
    a = numer1*denom2 + numer2*denom1
    b = denom1*denom2
    
    gcd = math.gcd(a,b)    
    while gcd != 1:
        a = a//gcd
        b = b//gcd
        gcd = math.gcd(a,b)
        if gcd == 1:
            break
    answer = [a , b]       
        
    
    return answer