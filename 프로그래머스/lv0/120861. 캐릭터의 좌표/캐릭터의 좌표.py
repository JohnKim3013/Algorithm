def solution(keyinput, board):
    answer = [0,0]
    w = board[0]
    h = board[1]
    for key in keyinput:
        if key == 'right' and answer[0]+1 <= (w//2):
            answer[0] += 1
        elif key == 'left' and answer[0]-1 >= -(w//2):
            answer[0] -= 1
        elif key == 'up' and answer[1]+1 <= (h//2):
            answer[1] += 1
        elif key == 'down' and answer[1]-1 >= -(h//2):
            answer[1] -= 1
    return answer