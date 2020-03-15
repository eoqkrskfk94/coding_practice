import sys
import copy
dir_y = [-1,1,0,0]
dir_x = [0,0,-1,1]
sys.setrecursionlimit(100000)
N = int(sys.stdin.readline())
max_height = 0
min_height = 100
board = []

for i in range(N):
  temp = list(map(int,sys.stdin.readline().split()))
  max_height = max(max_height, max(temp))
  min_height = min(min_height, min(temp))
  board.append(temp)


def dfs(y,x, rain_board,flag):

  if y < 0 or y >= N or x < 0 or x >= N:
    return
  
  if rain_board[y][x] == 0 or rain_board[y][x] == 2:
    return

  if rain_board[y][x] == 1:
    rain_board[y][x] = 2
    flag = 1

  for i in range(4):
    dfs(y+dir_y[i],x+dir_x[i],rain_board, flag)

  return flag

def bfs(y,x):
  queue = [[y,x]]
  rain_board[y][x] = 2

  while(queue):
    temp_y = queue[0][0]
    temp_x = queue[0][1]
    queue.pop(0)
    for i in range(4):
      ny = temp_y + dir_y[i]
      nx = temp_x + dir_x[i]
      if 0 <= ny < N and 0 <= nx < N and rain_board[ny][nx] == 1:
        rain_board[ny][nx] = 2
        queue.append([ny,nx])
      



  

flag = 0
answer = 1
for k in range(min_height,max_height):
  safe = 0
  rain_board = copy.deepcopy(board)
  for i in range(N):
    for j in range(N):
      if rain_board[i][j] <= k:
        rain_board[i][j] = 0
      else:
        rain_board[i][j] = 1
  
  for i in range(N):
    for j in range(N):
      if rain_board[i][j] == 1:
        #flag = dfs(i,j,rain_board,flag)
        bfs(i,j)
        safe += 1
        #if flag == 1:
        #  safe += 1


  answer = max(answer,safe)

print(answer)

       






