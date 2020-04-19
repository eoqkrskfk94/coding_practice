import sys

board = []
dir_y = [-1,1,0,0]
dir_x = [0,0,-1,1]

N,M = map(int, sys.stdin.readline().split())

for i in range(N):
  board.append(list(map(int,sys.stdin.readline().rstrip())))

count_board = [[0] * M for i in range(N)]
count_board[0][0] = 1



def bfs(start,count):
  queue =[start]
  board[0][0] = 0

  while(queue):
    y,x = queue.pop(0)

    for i in range(4):
      ny = y + dir_y[i]
      nx = x + dir_x[i]
    
      if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 1:
        count_board[ny][nx] = count_board[y][x] + 1
        board[ny][nx] = 0
        queue.append([ny,nx])

  

bfs([0,0],1)


print(count_board[N-1][M-1])

