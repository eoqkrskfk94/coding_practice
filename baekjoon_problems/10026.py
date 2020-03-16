import sys
import copy
sys.setrecursionlimit(100000)

dir_y = [-1,1,0,0]
dir_x = [0,0,-1,1]
N = int(sys.stdin.readline())

board1 = []

for i in range(N):
  temp = list(sys.stdin.readline().rstrip())
  board1.append(temp)

board2 = copy.deepcopy(board1)


def dfs_RGB(y,x,color,board):
  if y < 0 or y >= N or x < 0 or x >= N:
    return

  if board[y][x] == 'X' or board[y][x] != color:
    return
  
  if board[y][x] == color:
    board[y][x] = 'X'
  
  for i in range(4):
    dfs_RGB(y+dir_y[i],x+dir_x[i],color,board)

def bfs(y,x,color,board):
  queue = [[y,x]]

  while(queue):
    temp = queue.pop(0)

    for i in range(4):
      ny = dir_y[i] + temp[0]
      nx = dir_x[i] + temp[1]
      if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == color:
        board[ny][nx] = 'X'
        queue.append([ny,nx])

  

count = [0,0]
for i in range(N):
  for j in range(N):
    if board1[i][j] != 'X':
      #dfs_RGB(i,j,board1[i][j],board1)
      bfs(i,j,board1[i][j],board1)
      count[0] += 1

for i in range(N):
  for j in range(N):
    if board2[i][j] == 'G':
      board2[i][j] = 'R'


for i in range(N):
  for j in range(N):
    if board2[i][j] != 'X':
      #dfs_RGB(i,j,board2[i][j],board2)
      bfs(i,j,board2[i][j],board2)
      count[1] += 1


print(count[0], count[1])




