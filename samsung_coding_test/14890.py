import sys

N,L = map(int,sys.stdin.readline().split())
board = []
for i in range(N):
  board.append(list(map(int,sys.stdin.readline().split())))

answer = 0
for i in range(N):
  count = 1
  for j in range(N-1):
    if board[i][j] == board[i][j+1]:
      count += 1
    
    elif board[i][j] + 1 == board[i][j+1] and count >= L:
      count = 1
    
    elif board[i][j] - 1 == board[i][j+1] and count >= 0:
      count = (1 - L)
    
    else:
      count = -1
      break

  if count >= 0:
    answer += 1

    
for j in range(N):
  count = 1
  for i in range(N-1):
    if board[i][j] == board[i+1][j]:
      count += 1
    
    elif board[i][j] + 1 == board[i+1][j] and count >= L:
      count = 1
    
    elif board[i][j] - 1 == board[i+1][j] and count >= 0:
      count = (1 - L)
    
    else:
      count = -1
      break

  if count >= 0:
    answer += 1




print(answer)








