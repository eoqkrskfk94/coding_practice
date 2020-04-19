import sys
from collections import deque

board = []
dir_y = [-1,1,0,0]
dir_x = [0,0,-1,1]
q = deque()

M,N = map(int, sys.stdin.readline().split())
count_board = [[0] * M for i in range(N)]

for i in range(N):
  board.append(list(map(int,sys.stdin.readline().split())))
  for j in range(M):
    if board[i][j] == 1:
      q.append([i,j])
      count_board[i][j] = 1
    elif board[i][j] == -1:
      count_board[i][j] = -1


def bfs():

  while q:
    y,x = q.popleft()

    for i in range(4):
      ny = y + dir_y[i]
      nx = x + dir_x[i]

      if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 0:
        board[ny][nx] = -1
        count_board[ny][nx] = count_board[y][x] + 1
        q.append([ny,nx])

def check(count_board):
  answer = 0
  for i in range(N):
    for j in range(M):
      if count_board[i][j] == 0:
        return -1
      answer = max(answer, count_board[i][j])
  
  if answer == 1:
    return 0
  
  return answer-1


bfs()
print(check(count_board))









