def solution(num, k):
    num_list = list(map(int, str(num)))
    try:
        return num_list.index(k) + 1
    except:
        return -1
