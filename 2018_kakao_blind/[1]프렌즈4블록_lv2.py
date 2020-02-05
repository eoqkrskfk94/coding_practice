def solution(m, n, board):
    answer = 0
    new_board = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.insert(0,board[j][i])
        new_board.append(temp)
        
    while True:
        blocks = []
        for i in range(n-1):
            for j in range(m-1):
                if new_board[i][j] == new_board[i][j+1] and new_board[i][j] != 0:
                    if new_board[i][j] == new_board[i+1][j] and new_board[i+1][j] == new_board[i+1][j+1]:
                        block1, block2, block3, block4= [i,j], [i,j+1], [i+1,j], [i+1,j+1]
                        
                        if block1 not in blocks:
                            blocks.append(block1)
                        if block2 not in blocks:
                            blocks.append(block2)
                        if block3 not in blocks:
                            blocks.append(block3)
                        if block4 not in blocks:
                            blocks.append(block4)
        
        if not blocks:
            break
            
        blocks.sort(key=lambda x: x[1])
        for idx in reversed(blocks):
            new_board[idx[0]].pop(idx[1])
            new_board[idx[0]].append(0)
            answer += 1


    return answer
