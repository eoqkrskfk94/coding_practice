def solution(board, moves):
    answer = 0
    deep = len(board[0])
    box = []
    
    for move in moves:
        for i in range(deep):
            if board[i][move-1] != 0:
                box.append(board[i][move-1])
                board[i][move-1] = 0
                break
        
        if len(box) > 1:
            if box[-1] == box[-2]:
                box.pop()
                box.pop()
                answer += 2
    return answer
