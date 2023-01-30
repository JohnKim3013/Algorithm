def solution(rsp):
    table = str.maketrans('205','052')
    answer = rsp.translate(table)
    return answer