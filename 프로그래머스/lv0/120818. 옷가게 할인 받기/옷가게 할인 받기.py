def solution(price):
    if price < 100000:
        return int(price)
    elif price < 300000:
        return int(price * 0.95)
    elif price < 500000:
        return int(price * 0.90)
    else:
        return int(price * 0.80)